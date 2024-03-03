from typing import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import DB_PORT, DB_HOST, DB_NAME, DB_USER, DB_PASS

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
SessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, future=True)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
