"""
build_graph.py
--------------
Ingests AutoLISP function docs into a Kuzu graph database.
Only processes the ~558 docs that have *Supported Platforms:* markers
(function reference pages with structured metadata).

Uses Claude Haiku to extract entities and relationships from each file.

Usage:
    python build_graph.py --docs ./docs --db ./autolisp.db
    python build_graph.py --docs ./docs --db ./autolisp.db --limit 10
"""

import os
from dotenv import load_dotenv
import json
import re
import argparse
import hashlib
from pathlib import Path
from tqdm import tqdm
import kuzu
import anthropic
from sentence_transformers import SentenceTransformer

load_dotenv()

# -- Config --

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EXTRACTION_PROMPT = """\
You are processing AutoCAD/AutoLISP documentation. Extract structured data from
the markdown below. Return ONLY valid JSON with this exact schema:

{
  "entities": [
    {
      "name": "string",
      "type": "function|command|variable|concept|dialog|object",
      "summary": "string",
      "platform": "both|mac|windows_only",
      "mac_safe": true|false,
      "syntax": "string|null"
    }
  ],
  "relationships": [
    {
      "from": "entity_name",
      "to": "entity_name",
      "type": "calls|returns|parameter_of|alternative_to|related_to|requires"
    }
  ]
}

Rules:
- mac_safe=false for anything vlax-*, vlr-*, acet-*, vl-load-com
- platform="windows_only" for those same functions
- Extract ALL functions/commands mentioned, not just the primary one
- Keep summaries factual and brief

Markdown to process:
"""


# -- Database Schema --

def init_db(db_path: str) -> tuple:
    """Initialize Kuzu database and return (db, conn) tuple."""
    db = kuzu.Database(db_path)
    conn = kuzu.Connection(db)
    conn.execute("INSTALL vector; LOAD vector;")

    conn.execute("""
        CREATE NODE TABLE IF NOT EXISTS DocNode (
            id STRING PRIMARY KEY,
            name STRING,
            type STRING,
            summary STRING,
            platform STRING,
            mac_safe BOOLEAN,
            syntax STRING,
            embedding FLOAT[384],
            source_file STRING
        )
    """)

    conn.execute("""
        CREATE REL TABLE IF NOT EXISTS Relationship (
            FROM DocNode TO DocNode,
            type STRING
        )
    """)

    return db, conn


# -- Doc Filtering --

def has_platform_marker(filepath: Path) -> bool:
    """Check if a doc has a *Supported Platforms:* line (function reference)."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
        return "*Supported Platforms:*" in text
    except Exception:
        return False


# -- Extraction --

def extract_entities(content: str, client: anthropic.Anthropic) -> dict:
    """Call Claude Haiku to extract entities and relationships."""
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": EXTRACTION_PROMPT + content[:4000]
            }]
        )
        text = response.content[0].text.strip()
        text = re.sub(r"^```json\s*|```$", "", text, flags=re.MULTILINE).strip()
        return json.loads(text)
    except Exception as e:
        print(f"  Warning: Extraction failed: {e}")
        return {"entities": [], "relationships": []}


def make_node_id(name: str, source_file: str) -> str:
    """Stable unique ID for a node."""
    return hashlib.md5(f"{name}::{source_file}".encode()).hexdigest()[:16]


# -- Ingestion --

def ingest_docs(docs_dir: str, db_path: str, limit: int = 0):
    print(f"Initialising database at {db_path}")
    db, conn = init_db(db_path)

    print(f"Loading embedding model: {EMBEDDING_MODEL}")
    embedder = SentenceTransformer(EMBEDDING_MODEL)

    client = anthropic.Anthropic()

    # Find all markdown files, then filter to function reference docs
    all_md = list(Path(docs_dir).rglob("*.md"))
    print(f"Found {len(all_md)} total markdown files")

    md_files = [f for f in all_md if has_platform_marker(f)]
    print(f"Filtered to {len(md_files)} function reference docs (have *Supported Platforms:*)")

    if limit > 0:
        md_files = md_files[:limit]
        print(f"   (limited to {limit} files for testing)")

    node_registry = {}

    for md_file in tqdm(md_files, desc="Ingesting docs"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        if len(content.strip()) < 50:
            continue

        extracted = extract_entities(content, client)

        for entity in extracted.get("entities", []):
            name = entity.get("name", "").strip()
            if not name:
                continue

            node_id = make_node_id(name, str(md_file))
            node_registry[name] = node_id

            summary = entity.get("summary", "")
            embedding = embedder.encode(f"{name} {summary}").tolist()

            try:
                conn.execute("""
                    MERGE (n:DocNode {id: $id})
                    SET n.name = $name,
                        n.type = $type,
                        n.summary = $summary,
                        n.platform = $platform,
                        n.mac_safe = $mac_safe,
                        n.syntax = $syntax,
                        n.embedding = $embedding,
                        n.source_file = $source_file
                """, {
                    "id": node_id,
                    "name": name,
                    "type": entity.get("type", "function"),
                    "summary": summary,
                    "platform": entity.get("platform", "both"),
                    "mac_safe": entity.get("mac_safe", True),
                    "syntax": entity.get("syntax") or "",
                    "embedding": embedding,
                    "source_file": str(md_file)
                })
            except Exception as e:
                print(f"  Warning: Node insert failed for {name}: {e}")

        for rel in extracted.get("relationships", []):
            from_name = rel.get("from", "")
            to_name = rel.get("to", "")
            rel_type = rel.get("type", "related_to")

            if from_name in node_registry and to_name in node_registry:
                try:
                    conn.execute("""
                        MATCH (a:DocNode {id: $from_id}), (b:DocNode {id: $to_id})
                        MERGE (a)-[:Relationship {type: $type}]->(b)
                    """, {
                        "from_id": node_registry[from_name],
                        "to_id": node_registry[to_name],
                        "type": rel_type
                    })
                except Exception as e:
                    print(f"  Warning: Relationship insert failed: {e}")

    print(f"\nIngestion complete.")
    result = conn.execute("MATCH (n:DocNode) RETURN count(n)").get_next()
    print(f"   Nodes: {result[0]}")
    result = conn.execute("MATCH ()-[r:Relationship]->() RETURN count(r)").get_next()
    print(f"   Relationships: {result[0]}")

    print("Creating vector index...")
    try:
        conn.execute("""
            CALL CREATE_VECTOR_INDEX('DocNode', 'doc_vec_index', 'embedding')
        """)
        print("   Vector index created.")
    except Exception as e:
        print(f"   Warning: Vector index creation failed (may already exist): {e}")


# -- Entry Point --

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build GraphRAG database from AutoLISP docs")
    parser.add_argument("--docs", default="./docs", help="Path to docs directory")
    parser.add_argument("--db",   default="./autolisp.db", help="Output Kuzu DB path")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limit number of files to process (0 = all)")
    args = parser.parse_args()

    ingest_docs(args.docs, args.db, args.limit)
