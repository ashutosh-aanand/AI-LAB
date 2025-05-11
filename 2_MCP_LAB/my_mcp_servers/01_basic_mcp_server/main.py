from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mathmind")

# Addition tool
@mcp.tool()
def add(a: int, b: int) -> int : 
    """Add two numbers"""
    return a + b

# uv init .
# uv add "mcp[cli]"
# uv run mcp install main.py