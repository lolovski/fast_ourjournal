from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.school import School, Class
from app.requests.base import RequestsBase
from app.schemas.school import ClassCreate

school_requests = RequestsBase(School)
class_requests = RequestsBase(Class)


async def get_school_by_name(name: str, session: AsyncSession) -> School:

    school = await session.scalar(select(School).where(School.name == name))
    return school


async def create_class(class_: ClassCreate, session: AsyncSession) -> Class:
    class_data = class_.dict()
    class_ = Class(**class_data)
    session.add(class_)
    await session.commit()
    await session.refresh(class_)
    return class_


async def get_class_by_name(class_: ClassCreate, session: AsyncSession) -> Class:
    class_data = class_.dict()
    class_ = await session.scalar(select(Class).where(Class.name == class_data['name']).where(Class.school == class_data['school']))
    return class_


async def get_class_by_name_and_school(name: str, school: int, session: AsyncSession) -> Class:
    class_ = await session.scalar(select(Class).where(Class.name == name).where(Class.school == school))
    return class_

async def get_classes_in_school(school_id: int, session: AsyncSession) -> List[Class]:

    classes = await session.scalars(select(Class).where(Class.school == school_id))
    return classes.all()


async def get_class(class_id: int, session: AsyncSession) -> Class:

    class_ = await session.scalar(select(Class).where(Class.id == class_id))
    return class_


async def update_classes_in_school(classes, session: AsyncSession) -> list[Class]:
    for class_ in classes:
        if '11' in class_.name:
            await session.delete(class_)
        else:
            new_number = str(int(class_.name[:-1]) + 1)
            class_.name = new_number + class_.name[-1]
    await session.commit()


async def update_class(class_: Class, update, session: AsyncSession) -> Class:

    obj_data = class_.as_dict()
    update_data = update.dict(exclude_unset=True, exclude_none=True)
    for field in obj_data:
        if field in update_data:
            setattr(class_, field, update_data[field])
    session.add(class_)
    await session.commit()
    await session.refresh(class_)
    return class_


async def delete_class(
        class_: Class,
        session: AsyncSession
) -> Class:
    await session.delete(class_)
    await session.commit()
    return class_