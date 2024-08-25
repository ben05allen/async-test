from datetime import datetime
from sqlalchemy import Integer, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime


# Define your base model
class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )


class Address(BaseModel):
    __tablename__ = "addresses"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    street: Mapped[str]
    suite: Mapped[str]
    city: Mapped[str]
    zipcode: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="address")
    geo: Mapped["Geo"] = relationship(back_populates="address")


class Geo(BaseModel):
    __tablename__ = "geos"

    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))

    lat: Mapped[float]
    lng: Mapped[float]

    address: Mapped[Address] = relationship(back_populates="geo")


class Company(BaseModel):
    __tablename__ = "companies"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    name: Mapped[str]
    catchPhrase: Mapped[str]
    bs: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="company")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    username: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    website: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    address: Mapped[Address] = relationship(back_populates="user")
    company: Mapped[Company] = relationship(back_populates="user")
