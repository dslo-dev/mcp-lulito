from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import asyncio


async def main():

    server_params = StdioServerParameters(
        command="uv",
        args=[
            "run",
            "python",
            "server.py"
        ]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Herramientas disponibles:")

            for tool in tools.tools:
                print(
                    "-",
                    tool.name
                )


asyncio.run(main())