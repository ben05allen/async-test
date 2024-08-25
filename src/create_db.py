import asyncio
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine

from models import Base

load_dotenv()
# CONN_STR='mssql+aioodbc://[...]
CONN_STRING = os.environ["CONN_STR"]

engine = create_async_engine(CONN_STRING, echo=True)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
