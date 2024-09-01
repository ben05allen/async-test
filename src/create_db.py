import asyncio
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine

from models import Base

load_dotenv()
# CONN_STR='mssql+aioodbc://[...]
CONN_STR_BASE = os.environ["CONN_STR_BASE"]
PROJECT_FOLDER = os.environ["PROJECT_FOLDER"]
DATABASE = os.environ["DATABASE"]
CONN_STRING = f"{CONN_STR_BASE}{PROJECT_FOLDER}/{DATABASE}"

engine = create_async_engine(CONN_STRING, echo=True)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
