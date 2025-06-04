# server.py

### instructions to run this code:
# # 1. Install the MCP library: `uv install mcp[cli]`
# # 2. Save this code as `server.py`
## 3. Install the server dependencies:
# #    `uv install mcp[fastmcp]`
## 4 Install the mcp server.py file:
# #    `mcp install server.py`
## Next go in the Claude desktop and check the developer tools for the list of tools
## one should see `Demo` tool available in the list of tools



from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"