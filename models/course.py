from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class Course(Base, TimestampMixin):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(200))