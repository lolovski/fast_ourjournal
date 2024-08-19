from typing import Dict, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session
from passlib.context import CryptContext
from app.models.user import User
from app.models.school import School, Class
from app.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_username(username: str, session: AsyncSession) -> User:

    user = await session.scalar(select(User).where(User.username == username))
    if user is None:
        return None
    return user


async def create_user(user: UserCreate, session: AsyncSession) -> User:
    user_data = user.dict()
    user = User(**user_data, status=1)
    session.add(user)
    await session.commit()
    return user


async def get_users(session: AsyncSession):
    users = await session.scalars(select(User))
    return users.all()


async def get_user(user_id: int, session: AsyncSession) -> User:
    user = await session.scalars(select(User).where(User.id == user_id))
    return user




