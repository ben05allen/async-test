import asyncio
import aiohttp

from api import fetch_json
from schedules import User


async def main():
    # never actually do it this way ;)
    urls = [
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/users/2",
        "https://jsonplaceholder.typicode.com/users/3",
        "https://jsonplaceholder.typicode.com/users/4",
        "https://jsonplaceholder.typicode.com/users/5",
        "https://jsonplaceholder.typicode.com/users/6",
        "https://jsonplaceholder.typicode.com/users/7",
        "https://jsonplaceholder.typicode.com/users/8",
        "https://jsonplaceholder.typicode.com/users/9",
        "https://jsonplaceholder.typicode.com/users/10",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_json(session, url) for url in urls]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result in results:
            if isinstance(result, Exception):
                print(f"Error: {result}")
            else:
                user = User(**result)
                print(user)


if __name__ == "__main__":
    asyncio.run(main())
