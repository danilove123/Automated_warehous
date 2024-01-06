from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.asyncio import AsyncSession

from src.conf import DB_USER, DB_HOST, DB_PORT, DB_NAME, DB_PASS


engine = create_engine(
    url=f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True
)

async_engine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True
)

async_sessionmaker = sessionmaker(bind=async_engine, autocommit=False, autoflush=False, class_=AsyncSession)
sync_sessionmaker = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=Session)

