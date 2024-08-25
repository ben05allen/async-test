from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
CONN_STRING = os.environ["CONN_STRING"]


def get_session():
    engine = create_async_engine(CONN_STRING, future=True, echo=True)
    return sessionmaker(engine, expire_on_commit=False)
