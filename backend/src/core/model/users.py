from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import DATE

from backend.src.core.model.base import Base


class Users(Base):

    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str]
    age: Mapped[int]
    birthday: Mapped[DATE]
    photo: Mapped[str]
