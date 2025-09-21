from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select
from typing import List
from app.models.user  import User
from app.deps import get_db



app = FastAPI()

@app.get("/")
# def root():
#     return {"message": "Contract & Tax Compliance API running!"}
async def create_user(db: AsyncSession = Depends(get_db)):
    new_user = User(email="isba91@gmail.com", name="isba")
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user