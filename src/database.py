from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()
CONN_STRING = os.environ["CONN_STR"]


def get_session():
    engine = create_async_engine(CONN_STRING, echo=True)
    return async_sessionmaker(engine, expire_on_commit=False)
