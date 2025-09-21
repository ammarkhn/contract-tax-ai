from typing import AsyncGenerator
from app.db import AsyncSessionLocal

# Dependency for getting a DB session per request
async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as db:
        try:
            yield db              # Provide the session to the request
            await db.commit()     # Commit if everything goes fine
        except Exception:
            await db.rollback()   # Rollback if an error occurs
            raise
