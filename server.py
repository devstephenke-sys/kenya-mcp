"""Kenya MCP Server - Main entry point."""

from kenya_mcp.server import mcp

__all__ = ["mcp"]

if __name__ == "__main__":
    mcp.run()
