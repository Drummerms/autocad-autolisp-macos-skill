"""
build_graph.py
--------------
Ingests 4,500+ AutoLISP/AutoCAD markdown docs into a Kuzu graph database.
Uses Claude API to extract entities and relationships from each file.

Usage:
    python build_graph.py --docs ./docs --db ./autolisp.db

Requirements:
    pip install kuzu anthropic sentence-transformers tqdm
"""

import os
import json
import re
import argparse
import hashlib
from pathlib import Path
from tqdm import tqdm
import kuzu
import anthropic
from sentence_transformers import SentenceTransformer

# ── Config ────────────────────────────────────────────────────────────────────

EMBEDDING_MODEL = "all-MiniLM-L6-v2"   # Fast, local, good quality
BATCH_SIZE = 50                          # Files per extraction batch
EXTRACTION_PROMPT = """\
You are processing AutoCAD/AutoLISP documentation. Extract structured data from
the markdown below. Return ONLY valid JSON with this exact schema:

{
  "entities": [
    {
      "name": "string",           // e.g. "entmod", "vlax-get", "LAYER"
      "type": "function|command|variable|concept|dialog|object",
      "summary": "string",        // 1-2 sentence description
      "platform": "both|mac|windows_only",
      "mac_safe": true|false,
      "syntax": "string|null"     // function signature if present
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

# ── Database Schema ────────────────────────────────────────────────────────────

def init_db(db_path: str) -> kuzu.Connection:
    db = kuzu.Database(db_path)
    conn = kuzu.Connection(db)

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

    return conn


# ── Extraction ─────────────────────────────────────────────────────────────────

def extract_entities(content: str, client: anthropic.Anthropic) -> dict:
    """Call Claude to extract entities and relationships from a markdown doc."""
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",   # Fast + cheap for bulk ingestion
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": EXTRACTION_PROMPT + content[:4000]   # Truncate to fit context
            }]
        )
        text = response.content[0].text.strip()
        # Strip markdown fences if present
        text = re.sub(r"^```json\s*|```$", "", text, flags=re.MULTILINE).strip()
        return json.loads(text)
    except Exception as e:
        print(f"  ⚠️  Extraction failed: {e}")
        return {"entities": [], "relationships": []}


def make_node_id(name: str, source_file: str) -> str:
    """Stable unique ID for a node."""
    return hashlib.md5(f"{name}::{source_file}".encode()).hexdigest()[:16]


# ── Ingestion ──────────────────────────────────────────────────────────────────

def ingest_docs(docs_dir: str, db_path: str):
    print(f"🔧 Initialising database at {db_path}")
    conn = init_db(db_path)

    print(f"📦 Loading embedding model: {EMBEDDING_MODEL}")
    embedder = SentenceTransformer(EMBEDDING_MODEL)

    client = anthropic.Anthropic()   # Reads ANTHROPIC_API_KEY from env

    md_files = list(Path(docs_dir).rglob("*.md"))
    print(f"📂 Found {len(md_files)} markdown files\n")

    node_registry = {}   # name -> id, for relationship resolution

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
                print(f"  ⚠️  Node insert failed for {name}: {e}")

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
                    print(f"  ⚠️  Relationship insert failed: {e}")

    print(f"\n✅ Ingestion complete.")
    result = conn.execute("MATCH (n:DocNode) RETURN count(n)").get_next()
    print(f"   Nodes: {result[0]}")
    result = conn.execute("MATCH ()-[r:Relationship]->() RETURN count(r)").get_next()
    print(f"   Relationships: {result[0]}")


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build GraphRAG database from AutoLISP docs")
    parser.add_argument("--docs", default="./docs", help="Path to docs directory")
    parser.add_argument("--db",   default="./autolisp.db", help="Output Kuzu DB path")
    args = parser.parse_args()

    ingest_docs(args.docs, args.db)
