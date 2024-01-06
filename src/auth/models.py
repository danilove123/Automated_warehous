import datetime
from typing import Annotated

from sqlalchemy import MetaData, Integer, Column, String, Table, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata = MetaData()

strpk = Annotated[str,mapped_column(primary_key=True,nullable=False)]
intpk = Annotated[int,mapped_column(primary_key=True,nullable=False)]
strk = Annotated[str,mapped_column(primary_key=False,nullable=False)]
intk = Annotated[str,mapped_column(primary_key=False,nullable=False)]

timeutc = Annotated[datetime.datetime,mapped_column(
    server_default=text("TIMEZONE('utc',now())"),onupdate=datetime.datetime.utcnow
)]

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "Users"
    username: Mapped[strpk]
    age: Mapped[intk]
    email: Mapped[strk]
    hash_password: Mapped[strk]
    phone: Mapped[strk]

    def __str__(self):
        return self.__tablename__
