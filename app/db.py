# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import settings
DATABASE_URL = settings.DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# Create engine (connection to Postgres)
engine = create_async_engine(DATABASE_URL,  echo=True, future=True)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

# Base class for all models
class Base(DeclarativeBase):
    pass
