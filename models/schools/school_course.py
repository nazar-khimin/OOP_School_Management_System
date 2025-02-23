from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class SchoolCourse(Base, TimestampMixin):
    __tablename__ = "school_courses"

    # Explicitly set the column names to avoid conflicts
    course_id: Mapped[str] = mapped_column("course_id", String, ForeignKey('courses.id'))
    school_id: Mapped[str] = mapped_column("school_id", String, ForeignKey('schools.id'))

    school: Mapped['School'] = relationship('School', back_populates='school_courses')
    course: Mapped['Course'] = relationship('Course', back_populates='school_courses')
