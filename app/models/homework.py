import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import Column, String, Text, Integer, ForeignKey, DateTime, func

from app.db.base_class import Base
now = datetime.datetime.now().date()


class Homework(Base):
    __tablename__ = 'homework'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    class_user: Mapped[int] = mapped_column(ForeignKey('class.id'))
    text: Mapped[str] = mapped_column(Text)
    shedule: Mapped[int] = mapped_column(ForeignKey('shedule.id'))
    author: Mapped[int] = mapped_column(ForeignKey('user.id'))
    week: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.date(now.year, now.month, now.day - now.weekday()))
    weekday: Mapped[str] = mapped_column(String(32), nullable=True)


class Comment(Base):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text)
    author: Mapped[int] = mapped_column(ForeignKey('user.id'))
    homework: Mapped[int] = mapped_column(ForeignKey('homework.id'))
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class HomeworkPhoto(Base):
    __tablename__ = 'homework_photo'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), default='Фото')
    file_path: Mapped[str] = mapped_column(String(256))
    user: Mapped[int] = mapped_column(ForeignKey('user.id'))
    homework: Mapped[int] = mapped_column(ForeignKey('homework.id'))
    public_id: Mapped[str] = mapped_column(String(256), nullable=True)
    pub_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

