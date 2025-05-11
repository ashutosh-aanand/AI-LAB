Learning to create an mcp server:
---

MCP is an open protocol designed to standardize how applications provide context to AI models. 

It allows applications to expose data and functionality to AI models in a structured way, similar to how APIs work but specifically tailored for AI interactions.

---

We will use mcp python sdk

install uv
- package manager better than pip
- don't install using pip
- install here :
    - https://docs.astral.sh/uv/getting-started/installation/
    - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

install claude desktop
- https://claude.ai/download

we will be adding our mcp server to claude desktop and 
will see its LLMs interacting with our MCP server's methods.

in 01_basic_mcp_server

    - `uv init .` -> this initialises a new uv project
    - `uv add "mcp[cli]"` -> installs the mcp[cli] dependency

Now in main.py

Create a mcp tool

```
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Mathmind")

# Addition tool
@mcp.tool()
def add(a: int, b: int) -> int : 
    """Add two numbers"""
    return a + b
```

Now we need to start this server and install it in Claude:
run `uv run mcp install main.py`

[05/11/25 15:29:43] INFO     Added server 'Mathmind' to Claude config                                   claude.py:141                    INFO     Successfully installed Mathmind in Claude app

Now for this to reflect in Claude, close the claude form task manager and restart it.

Now ask claude to add 2 and 3. It will call our mcp server Mathmind's add tool and return the result.
👏


References:
- video: https://www.youtube.com/watch?v=-8k9lGpGQ6g
- documentation: https://github.com/modelcontextprotocol/python-sdk

