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

class Pallet(Base):
    __tablename__ = "Pallet"
    id_producer: Mapped[strpk]
    type: Mapped[strk]
    id_product: Mapped[strpk]
    id_pallet: Mapped[strpk]


class Shelf(Base):
    __tablename__ = "Shelf"
    id_cell: Mapped[strpk]
    id_pallet:Mapped[strpk]
    id_producer:Mapped[strpk]
    added_at:Mapped[timeutc]

class Producers(Base):
    __tablename__ = "Producers"
    id_producer:Mapped[strpk]
    name:Mapped[strk]

class Staff(Base):
    __tablename__ = "Staff"
    id_staff:Mapped[strpk]
    name:Mapped[strk]
    specification:Mapped[strk]