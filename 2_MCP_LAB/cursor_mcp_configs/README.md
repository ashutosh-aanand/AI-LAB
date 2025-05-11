# Cursor mcp servers
---

What are mcp servers ?

- MCP(model context protocol) is a way to write the methods/functions and expose them to the LLMs. 
- Exposing methods/functions via MCP to LLMs allows the models to call these functions directly, enabling them to perform actions, retrieve data, or interact with external systems via api calls etc., real time. 
- This makes LLMs much more powerful and interactive, as they can go beyond just generating text -- they can execute code, access APIs, and provide dynamic latest responses by leveraging the exposed functions.

What Cursor has to do with MCP servers ?

- Cursor connects to MCP serves so LLMs can use the exposed functions directly within the editor, enabling real-time code execution and enhanced interactivity.

---

Open source cursor servers:
---



1. coincap-mcp
   - Functions available:
     - bitcoin_price
     - get_crypto_price 
     - list_assets


References:
---

https://docs.cursor.com/context/model-context-protocol

https://github.com/punkpeye/awesome-mcp-servers
https://smithery.ai/
