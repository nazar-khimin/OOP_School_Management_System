
from sqlalchemy import Uuid, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class StudentCourse(Base, TimestampMixin):
    __tablename__ = "student_courses"
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))
    student_id: Mapped[str] = mapped_column(Uuid, ForeignKey('students.id'))


    course: Mapped['Course'] = relationship('Course', back_populates='student_courses')
    student: Mapped['Student'] = relationship('Student', back_populates='student_courses')