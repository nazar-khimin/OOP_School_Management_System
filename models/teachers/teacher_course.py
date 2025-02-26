
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class TeacherCourse(Base, TimestampMixin):
    __tablename__ = "teacher_courses"
    teacher_id: Mapped[str] = mapped_column(String, ForeignKey('teachers.id'))
    course_id: Mapped[str] = mapped_column(String, ForeignKey('courses.id'))

    course: Mapped['Course'] = relationship('Course', back_populates='teacher_courses')
    teacher: Mapped['Teacher'] = relationship('Teacher', back_populates='teacher_courses')