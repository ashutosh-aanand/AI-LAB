Learning to create an mcp server:
---

we will use mcp python sdk

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
    - `uv add "mcp[cli]"`



References:
- video: https://www.youtube.com/watch?v=-8k9lGpGQ6g
