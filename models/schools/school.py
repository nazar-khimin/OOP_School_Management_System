from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class School(Base, TimestampMixin):
    __tablename__ = "schools"
    name: Mapped[str] = mapped_column(String(30))

    school_courses: Mapped[list['SchoolCourse']] = relationship('SchoolCourse', back_populates='school')
    students: Mapped[list['Student']] = relationship('Student', back_populates='school')