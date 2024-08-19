from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import Column, String, Text, Integer, ForeignKey

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column(String(128))
    last_name: Mapped[str] = mapped_column(String(64))
    first_name: Mapped[str] = mapped_column(String(64))
    middle_name: Mapped[str] = mapped_column(String(64), nullable=True)
    telegram_id: Mapped[str] = mapped_column(String(64), nullable=True)
    status: Mapped[int] = mapped_column(ForeignKey('status.id'))
    class_user: Mapped[int] = mapped_column(ForeignKey('class.id'))


class Status(Base):
    __tablename__ = 'status'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(128))
