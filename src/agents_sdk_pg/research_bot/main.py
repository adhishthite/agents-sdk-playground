import asyncio

from manager import ResearchManager

import os
from dotenv import load_dotenv

load_dotenv()

async def main() -> None:
    query = input("What would you like to research? ")
    await ResearchManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())