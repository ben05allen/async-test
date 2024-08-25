import asyncio
import aiohttp
from sqlalchemy import select

from api import fetch_json
from database import get_session
import models
import schedules
from write import add_user


async def add_users():
    AsyncSession = await get_session()

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
                user = schedules.User(**result)
                async with AsyncSession() as session:
                    await add_user(user, session)


async def select_user(username: str) -> models.User | None:
    AsyncSession = await get_session()

    async with AsyncSession() as session:
        stmt = select(models.User).where(models.User.username == username).limit(1)

        result = await session.execute(stmt)

        select_user = result.scalars().first()

        return select_user


async def main():
    # await add_users()

    print(await select_user("Kamren"))
    print(await select_user("Kamrentypo"))


if __name__ == "__main__":
    asyncio.run(main())
