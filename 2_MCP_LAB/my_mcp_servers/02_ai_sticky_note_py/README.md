https://composio.dev/blog/mcp-server-step-by-step-guide-to-building-from-scrtch/

setup:
---
python -m venv dotenv
dotenv\\Scripts\\activate
pip install mcp mcp[cli]


running:
---
mcp dev main.py


Working mcp.json file
```
{
  "mcpServers": {
    "NotesMan": {
      "command": "C:\\Users\\ashut\\Desktop\\ai\\02_ai_sticky_note_py\\dotenv\\Scripts\\python.exe C:\\Users\\ashut\\Desktop\\ai\\02_ai_sticky_note_py\\main.py"
    },
    "NotesMan2": {
      "command": "F:\\Web Development\\github_folder\\AI-LAB\\2_MCP_LAB\\my_mcp_servers\\02_ai_sticky_note_py\\dotenv\\Scripts\\python.exe F:\\Web Development\\github_folder\\AI-LAB\\2_MCP_LAB\\my_mcp_servers\\02_ai_sticky_note_py\\main.py"
    }
  }
}
```