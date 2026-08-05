from mcp.server.fastmcp import FastMCP

from tools.users import get_user
from tools.tasks import create_task, list_tasks


mcp = FastMCP("lulito")


@mcp.tool()
def find_user(external_id: str):
    return get_user(external_id)


@mcp.tool()
def add_task(
    user_id: int,
    title: str,
    description: str | None = None
):
    return create_task(
        user_id,
        title,
        description
    )


@mcp.tool()
def get_tasks(user_id: int):
    return list_tasks(user_id)


if __name__ == "__main__":
    print("MCP Lulito iniciado")
    mcp.run()