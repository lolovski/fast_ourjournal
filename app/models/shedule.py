from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import Column, String, Text, Integer, ForeignKey

from app.db.base_class import Base


class Lesson(Base):
    __tablename__ = 'lesson'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))


class Day(Base):
    __tablename__ = 'day'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(16))


class Shedule(Base):
    __tablename__ = 'shedule'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    class_user: Mapped[int] = mapped_column(ForeignKey('class.id'))
    lesson: Mapped[int] = mapped_column(ForeignKey('lesson.id'))
    day: Mapped[int] = mapped_column(ForeignKey('day.id'))
    number: Mapped[int] = mapped_column(Integer, default=0)

