from typing import Optional

from fastapi import Body
from pydantic import BaseModel, Field, validator


class SchoolCreate(BaseModel):
    name: str = Field(
        ..., min_length=2, max_length=64,
    )


class SchoolRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ClassCreate(BaseModel):
    name: str = Field(
        ..., min_length=2, max_length=32,
    )
    school: int
    count_students: int = Field(
        ..., gt=1, lt=64,
    )


class ClassRead(BaseModel):
    id: int
    name: str
    school: int
    count_students: int

    class Config:
        orm_mode = True


class ClassUpdate(BaseModel):
    name: Optional[str] = Body(None)
    school: Optional[int] = Body(None)
    count_students: Optional[int] = Body(None, gt=0, lt=100)

    @validator('name')
    def name_must_not_none(cls, value):
        if value is None:
            raise ValueError('Имя не может быть пустым!')

"""    @validator('count_students')
    def count_students_must_not_none(cls, value):
        if value < 1:
            raise ValueError('Количество учеников не может быть < 1')"""


