from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

load_dotenv()
CONN_STRING = os.environ["CONN_STR"]


async def get_session() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(CONN_STRING, echo=True)
    return async_sessionmaker(engine, expire_on_commit=False)
