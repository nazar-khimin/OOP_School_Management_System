from sqlalchemy import Uuid, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from models.base import Base
from models.schools.school_course import SchoolCourse
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class School(Base, TimestampMixin):
    __tablename__ = "schools"
    name: Mapped[str] = mapped_column(String(30))

    school_courses: Mapped[list['SchoolCourse']] = relationship('SchoolCourse', back_populates='school')