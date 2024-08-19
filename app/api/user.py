from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Body
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayLookup, DisplayMode
from fastui.events import BackEvent, GoToEvent
from fastui.forms import fastui_form

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse

from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.requests.user import get_user_by_username, create_user, get_users, get_user
from app.core.examples import user_create_examples
from app.db.session import get_async_session
router = APIRouter()


@router.post(
    '/',
    response_model=UserRead,
    response_description='Краткое описаие пользователя',
    summary='Создание нового пользователя',
    response_model_exclude_none=True,
)
async def create_user_api(
        user: UserCreate = Body(..., openapi_examples=user_create_examples),
        session: AsyncSession = Depends(get_async_session),
):
    """
        Создание пользователя:

        - **username**: ник
        - **password**: пароль
        - **last_name**: фамилия
        - **first_name**: имя
        - **middle_name**: отчество
        - **class_user**: ID класса
        """
    db_user = await get_user_by_username(user.username, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail='User already registered')
    db_user = await create_user(user, session=session)
    return db_user

