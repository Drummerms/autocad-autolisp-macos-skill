"""
mcp_server.py
-------------
FastMCP server exposing GraphRAG search over the AutoLISP knowledge graph.
Claude calls this tool during skill execution instead of reading local docs.

Usage:
    AUTOLISP_DB_PATH=./autolisp.db python mcp_server.py

Configure in Claude Code via .mcp.json (auto-discovered).
"""

import os
from typing import Optional
import kuzu
from sentence_transformers import SentenceTransformer
from mcp.server.fastmcp import FastMCP

# -- Init --

DB_PATH = os.environ.get("AUTOLISP_DB_PATH", "./autolisp.db")

print(f"Loading graph DB from {DB_PATH}...")
db = kuzu.Database(DB_PATH)
conn = kuzu.Connection(db)
conn.execute("INSTALL vector; LOAD vector;")

print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

mcp = FastMCP("autolisp_docs")

# -- Helpers --


def vector_search(query: str, top_k: int = 8) -> list[dict]:
    """Find semantically similar nodes using vector index."""
    query_embedding = embedder.encode(query).tolist()

    result = conn.execute(f"""
        CALL QUERY_VECTOR_INDEX('DocNode', 'doc_vec_index', $embedding, {top_k})
        WITH node, distance
        RETURN node.id, node.name, node.type, node.summary, node.platform,
               node.mac_safe, node.syntax, node.source_file, distance
        ORDER BY distance ASC
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

    result = conn.execute(f"""
        MATCH (seed:DocNode)-[:Relationship*1..{depth}]->(n:DocNode)
        WHERE seed.id IN $seed_ids
        RETURN DISTINCT n.id, n.name, n.type, n.summary,
                        n.platform, n.mac_safe, n.syntax
    """, {"seed_ids": node_ids})

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
    mac_tag = "Mac-safe" if node.get("mac_safe") else "Windows only"
    platform = node.get("platform", "unknown")
    syntax = f"\n  Syntax:   {node['syntax']}" if node.get("syntax") else ""
    score = f"  [distance: {node['score']}]" if "score" in node else ""
    prefix = f"[{label}] " if label else ""

    return (
        f"{prefix}**{node['name']}** ({node['type']}) -- {mac_tag} | platform: {platform}{score}"
        f"\n  Summary:  {node.get('summary', 'N/A')}"
        f"{syntax}"
    )


# -- MCP Tool --

@mcp.tool()
def search(
    query: str,
    depth: int = 2,
    filter: Optional[str] = None
) -> str:
    """
    Search the AutoLISP/AutoCAD documentation knowledge graph.

    Args:
        query:  What you want to know -- function name, concept, question,
                or a list of function names separated by spaces.
        depth:  Graph traversal depth after vector search seed.
                1 = direct matches only (fast)
                2 = matches + related functions/commands (default)
                3 = broad exploration -- use for architectural questions
        filter: Optional platform filter.
                "mac"          -> only Mac-safe nodes
                "windows_only" -> only Windows-only nodes
                "both"         -> no filter (default)

    Returns:
        Formatted documentation context with platform compatibility info.
    """
    depth = max(1, min(depth, 3))

    seeds = vector_search(query, top_k=8)

    if not seeds:
        return f"No documentation found matching: {query}"

    if filter == "mac":
        seeds = [n for n in seeds if n.get("mac_safe") is True]
    elif filter == "windows_only":
        seeds = [n for n in seeds if n.get("mac_safe") is False]

    neighbors = []
    if depth >= 2:
        seed_ids = [n["id"] for n in seeds]
        raw_neighbors = graph_expand(seed_ids, depth - 1)

        if filter == "mac":
            raw_neighbors = [n for n in raw_neighbors if n.get("mac_safe") is True]
        elif filter == "windows_only":
            raw_neighbors = [n for n in raw_neighbors if n.get("mac_safe") is False]

        seed_ids_set = {n["id"] for n in seeds}
        neighbors = [n for n in raw_neighbors if n["id"] not in seed_ids_set]

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


# -- Run --

if __name__ == "__main__":
    mcp.run()
