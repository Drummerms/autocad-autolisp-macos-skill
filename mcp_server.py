"""
mcp_server.py
-------------
FastMCP server exposing GraphRAG search over the AutoLISP knowledge graph.
Claude calls this tool during skill execution instead of reading local docs.

Usage:
    pip install mcp sentence-transformers kuzu
    python mcp_server.py

Configure in Claude Code / Claude Desktop:
    {
      "mcpServers": {
        "autolisp_docs": {
          "command": "python3",
          "args": ["/path/to/mcp_server.py"],
          "env": { "AUTOLISP_DB_PATH": "/path/to/autolisp.db" }
        }
      }
    }
"""

import os
import json
from typing import Optional
import kuzu
from sentence_transformers import SentenceTransformer
from mcp.server.fastmcp import FastMCP

# ── Init ───────────────────────────────────────────────────────────────────────

DB_PATH = os.environ.get("AUTOLISP_DB_PATH", "./autolisp.db")

print(f"Loading graph DB from {DB_PATH}...")
db = kuzu.Database(DB_PATH)
conn = kuzu.Connection(db)

print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

mcp = FastMCP("autolisp_docs")

# ── Helpers ────────────────────────────────────────────────────────────────────

def vector_search(query: str, top_k: int = 8) -> list[dict]:
    """Find semantically similar nodes using cosine similarity."""
    query_embedding = embedder.encode(query).tolist()

    # Kuzu supports manual cosine similarity via list_cosine_similarity
    result = conn.execute(f"""
        MATCH (n:DocNode)
        WITH n,
             list_cosine_similarity(n.embedding, $embedding) AS score
        WHERE score > 0.3
        RETURN n.id, n.name, n.type, n.summary, n.platform,
               n.mac_safe, n.syntax, n.source_file, score
        ORDER BY score DESC
        LIMIT {top_k}
    """, {"embedding": query_embedding})

    nodes = []
    while result.has_next():
        row = result.get_next()
        nodes.append({
            "id":          row[0],
            "name":        row[1],
            "type":        row[2],
            "summary":     row[3],
            "platform":    row[4],
            "mac_safe":    row[5],
            "syntax":      row[6],
            "source_file": row[7],
            "score":       round(row[8], 3)
        })
    return nodes


def graph_expand(node_ids: list[str], depth: int) -> list[dict]:
    """Traverse the graph outward from seed nodes up to `depth` hops."""
    if not node_ids or depth < 1:
        return []

    id_list = json.dumps(node_ids)

    result = conn.execute(f"""
        MATCH (seed:DocNode)
        WHERE seed.id IN {id_list}
        CALL bfs(seed, {depth}, 'Relationship') YIELD node AS n
        RETURN DISTINCT n.id, n.name, n.type, n.summary,
                        n.platform, n.mac_safe, n.syntax
    """)

    neighbors = []
    while result.has_next():
        row = result.get_next()
        neighbors.append({
            "id":       row[0],
            "name":     row[1],
            "type":     row[2],
            "summary":  row[3],
            "platform": row[4],
            "mac_safe": row[5],
            "syntax":   row[6]
        })
    return neighbors


def format_node(node: dict, label: str = "") -> str:
    """Format a node for readable output to Claude."""
    mac_tag = "✅ Mac-safe" if node.get("mac_safe") else "❌ Windows only"
    platform = node.get("platform", "unknown")
    syntax = f"\n  Syntax:   {node['syntax']}" if node.get("syntax") else ""
    score = f"  [score: {node['score']}]" if "score" in node else ""
    prefix = f"[{label}] " if label else ""

    return (
        f"{prefix}**{node['name']}** ({node['type']}) — {mac_tag} | platform: {platform}{score}"
        f"\n  Summary:  {node.get('summary', 'N/A')}"
        f"{syntax}"
    )


# ── MCP Tool ───────────────────────────────────────────────────────────────────

@mcp.tool()
def search(
    query: str,
    depth: int = 2,
    filter: Optional[str] = None
) -> str:
    """
    Search the AutoLISP/AutoCAD documentation knowledge graph.

    Args:
        query:  What you want to know — function name, concept, question,
                or a list of function names separated by spaces.
        depth:  Graph traversal depth after vector search seed.
                1 = direct matches only (fast)
                2 = matches + related functions/commands (default)
                3 = broad exploration — use for architectural questions
        filter: Optional platform filter.
                "mac"          → only Mac-safe nodes
                "windows_only" → only Windows-only nodes
                "both"         → no filter (default)

    Returns:
        Formatted documentation context with platform compatibility info.
    """
    depth = max(1, min(depth, 3))   # Clamp to 1–3

    # Step 1: Vector search for seed nodes
    seeds = vector_search(query, top_k=8)

    if not seeds:
        return f"No documentation found matching: {query}"

    # Step 2: Apply platform filter to seeds
    if filter == "mac":
        seeds = [n for n in seeds if n.get("mac_safe") is True]
    elif filter == "windows_only":
        seeds = [n for n in seeds if n.get("mac_safe") is False]

    # Step 3: Graph expansion
    neighbors = []
    if depth >= 2:
        seed_ids = [n["id"] for n in seeds]
        raw_neighbors = graph_expand(seed_ids, depth - 1)

        # Apply filter to neighbors too
        if filter == "mac":
            raw_neighbors = [n for n in raw_neighbors if n.get("mac_safe") is True]
        elif filter == "windows_only":
            raw_neighbors = [n for n in raw_neighbors if n.get("mac_safe") is False]

        # Deduplicate against seeds
        seed_ids_set = {n["id"] for n in seeds}
        neighbors = [n for n in raw_neighbors if n["id"] not in seed_ids_set]

    # Step 4: Format output
    lines = [
        f"## GraphRAG Results for: `{query}`",
        f"_Depth: {depth} | Filter: {filter or 'none'} | "
        f"Seeds: {len(seeds)} | Related: {len(neighbors)}_\n",
        "### Direct Matches\n"
    ]

    for node in seeds[:6]:
        lines.append(format_node(node, label="MATCH"))
        lines.append("")

    if neighbors:
        lines.append(f"\n### Related Nodes (graph neighbors)\n")
        for node in neighbors[:10]:
            lines.append(format_node(node, label="RELATED"))
            lines.append("")

    return "\n".join(lines)


# ── Run ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
