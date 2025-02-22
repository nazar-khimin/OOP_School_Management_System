from sqlalchemy import Uuid, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from models.base import Base
from models.course import Course
from models.schools.school import School
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class SchoolCourse(Base, TimestampMixin):
    __tablename__ = "school_courses"
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))

    school: Mapped['School'] = relationship('School', back_populates='school_courses')
    course: Mapped['Course'] = relationship('Course', back_populates='school_courses')
