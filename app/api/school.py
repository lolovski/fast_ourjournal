from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session
from app.requests.school import (create_class,
                                 get_classes_in_school, get_class_by_name,
                                 get_class, update_classes_in_school,
                                 update_class, get_class_by_name_and_school, delete_class,
                                 school_requests)
from app.schemas.school import SchoolCreate, SchoolRead, ClassRead, ClassCreate, ClassUpdate

router = APIRouter()


@router.get(
    "/",
    tags=["school"],
    response_model=List[SchoolRead],
)
async def get_schools_api(
        session: AsyncSession = Depends(get_async_session),
):
    schools = await school_requests.get_multi(session)
    if schools is None:
        raise HTTPException(404, detail="Schools not found")
    return schools


@router.post(
    "/",
    tags=["school"],
    response_model=SchoolRead,
)
async def create_school_api(
    school: SchoolCreate,
    session: AsyncSession = Depends(get_async_session),
):
    db_school = await school_requests.create(obj_in=school, session=session)
    return db_school


@router.get(
    '/{school_id}',
    tags=["school"],
    response_model=SchoolRead,
)
async def get_school_api(
    school_id: int = Path(...),
    session: AsyncSession = Depends(get_async_session),
):
    school = await school_requests.get(school_id, session=session)
    if school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@router.get(
    '/class/{class_id}',
    tags=["class"],
    response_model=ClassRead,
)
async def get_class_api(
    class_id: int = Path(...),
    session: AsyncSession = Depends(get_async_session),
):
    class_ = await check_class_exists(class_id, session=session)
    return class_


@router.get(
    '/classes/{school_id}',
    tags=["class"],
    response_model=List[ClassRead],
)
async def get_class_in_school_api(
    school_id: int = Path(...),
    session: AsyncSession = Depends(get_async_session),
):
    classes = await get_classes_in_school(school_id, session=session)
    if classes is None:
        raise HTTPException(status_code=404, detail="Classes not found")
    return classes


@router.post(
    '/class/',
    tags=["class"],
    response_model=ClassRead,
)
async def create_class_api(
    class_: ClassCreate,
    session: AsyncSession = Depends(get_async_session),
):
    db_class = await get_class_by_name(class_, session=session)
    if db_class is not None:
        raise HTTPException(status_code=400, detail="Class already registered")
    db_class = await create_class(class_, session=session)
    return db_class


@router.patch(
    '/classes/{school_id}',
    tags=["class"],
    response_model=List[ClassRead],
    response_model_exclude_none=True,
)
async def update_classes_in_school_api(
        school_id: int = Path(...),
        session: AsyncSession = Depends(get_async_session),
):
    classes = await get_classes_in_school(school_id, session=session)
    if not classes:
        raise HTTPException(status_code=404, detail="Classes not found")
    await update_classes_in_school(classes=classes, session=session)
    return await get_classes_in_school(school_id, session=session)


@router.patch(
    '/class/{class_id}',
    tags=["class"],
    response_model=ClassRead,
)
async def update_class_api(
        class_id: int,
        update_in: ClassUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    class_ = await check_class_exists(class_id, session=session)
    if update_in.name is not None:
        if update_in.school is not None:
            await check_class_name_duplicate(name=update_in.name, school=update_in.school, session=session)
        else:
            await check_class_name_duplicate(name=update_in.name, school=class_.school, session=session)
    class_ = await update_class(class_, update_in, session=session)
    return class_


async def check_class_name_duplicate(
    name: str,
    school: int,
    session: AsyncSession = Depends(get_async_session),
) -> None:
    duplicate_class = await get_class_by_name_and_school(name=name, school=school, session=session)
    if duplicate_class is not None:
        raise HTTPException(status_code=400, detail="Class already registered")



@router.delete(
    '/class/{class_id}',
    tags=["class"],
    response_model=ClassRead,
    response_model_exclude_none=True,
)
async def delete_class_api(
        class_id: int = Path(...),
        session: AsyncSession = Depends(get_async_session),
):
    class_ = await check_class_exists(class_id, session=session)
    class_ = await delete_class(class_, session=session)
    return class_


async def check_class_exists(
        class_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    class_ = await get_class(class_id, session=session)
    if class_ is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_


