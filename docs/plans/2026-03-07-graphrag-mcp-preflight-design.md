# GraphRAG MCP Pre-flight Fix & Test Design

**Date:** 2026-03-07
**Status:** Approved
**Prerequisite:** `docs/plans/2026-03-07-graphrag-mcp-integration-design.md`

## Summary

Fix 5 critical bugs in `build_graph.py` and `mcp_server.py` discovered via Kuzu API documentation review, then run a full end-to-end pre-flight test with a small doc subset before committing to the full 4,500+ doc ingestion.

## Bugs Found

### Bug 1: Missing vector extension initialization
- **Files:** `build_graph.py:init_db()`, `mcp_server.py` init block
- **Issue:** Neither file calls `INSTALL vector; LOAD vector;` which Kuzu requires before using `FLOAT[384]` embeddings and similarity functions
- **Fix:** Add `conn.execute("INSTALL vector; LOAD vector;")` after creating the connection, before any table creation or querying

### Bug 2: Wrong vector similarity function name
- **File:** `mcp_server.py:52`
- **Issue:** Uses `list_cosine_similarity()` which doesn't exist in Kuzu
- **Fix:** Replace with `ARRAY_COSINE_SIMILARITY()`

### Bug 3: `CALL bfs()` doesn't exist in Kuzu
- **File:** `mcp_server.py:85-91`
- **Issue:** Uses `CALL bfs(seed, depth, 'Relationship')` which is not a Kuzu procedure
- **Fix:** Replace with Kuzu's variable-length relationship pattern:
  ```cypher
  MATCH (seed:DocNode)-[:Relationship*1..N]->(n:DocNode)
  WHERE seed.id IN $seed_ids
  RETURN DISTINCT n.id, n.name, n.type, n.summary, n.platform, n.mac_safe, n.syntax
  ```

### Bug 4: No vector index created
- **File:** `build_graph.py` (end of `ingest_docs`)
- **Issue:** Embeddings are stored but no vector index is created, forcing brute-force scans
- **Fix:** Add `CREATE_VECTOR_INDEX('DocNode', 'doc_vec_index', 'embedding')` after ingestion. Update `mcp_server.py:vector_search` to use `QUERY_VECTOR_INDEX`.

### Bug 5: Unsafe f-string interpolation in graph_expand
- **File:** `mcp_server.py:83-91`
- **Issue:** `id_list = json.dumps(node_ids)` injected via f-string instead of parameterized query
- **Fix:** Use `$seed_ids` parameter

## Additional Changes

- Add `.env` loading (python-dotenv or manual) to `build_graph.py` so it picks up `ANTHROPIC_API_KEY` from `.env`
- Add `--limit N` flag to `build_graph.py` for testing with a doc subset
- Add `python-dotenv` to `requirements.txt`

## Test Plan

After applying all fixes:

1. **Install deps:** `pip install -r requirements.txt`, verify all imports
2. **Set API key:** Fill in `.env` with real `ANTHROPIC_API_KEY`
3. **Test ingestion:** `python3 build_graph.py --docs ./docs --db ./test_autolisp.db --limit 10`
4. **Verify DB populated:** Query node and relationship counts
5. **Test vector search:** Run `QUERY_VECTOR_INDEX` query directly
6. **Test graph traversal:** Run variable-length path query directly
7. **Test MCP server:** Start server, invoke search tool, verify response
8. **Cleanup:** Remove `test_autolisp.db/`

## Approach

Fix-then-test (Approach A): Fix all known bugs first, then run full pre-flight. Avoids debugging known failures during testing.
