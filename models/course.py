from typing import Optional

from sqlalchemy import String, Uuid, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class Courses(Base, TimestampMixin):
    __tablename__ = 'courses'
    name: Mapped[str] = mapped_column(String(30))
    teacher_id: Mapped[str] = mapped_column(Uuid, ForeignKey('teachers.id'))
    max_capacity: Mapped[int] = mapped_column(Integer)
    required_grade_level: Mapped[int] = mapped_column(Integer)
    credits: Mapped[int] = mapped_column(Integer)
