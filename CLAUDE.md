## Tooling
- This project uses uv. Never call `python`, `python3` or `pip` directly.
  - Run scripts: `uv run <file>.py`
  - Add deps: `uv add <pkg>` (not pip install)
  - MCP inspector: `uv run mcp dev mcp_server.py`
