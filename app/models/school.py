from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import Column, String, Text, Integer, ForeignKey

from app.db.base_class import Base


class School(Base):
    __tablename__ = 'school'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))


class Class(Base):
    __tablename__ = 'class'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    school: Mapped[int] = mapped_column(Integer, ForeignKey('school.id'))
    count_students: Mapped[int] = mapped_column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


