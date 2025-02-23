from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class StudentGrade(Base, TimestampMixin):
    __tablename__ = "student_grades"
    course_id: Mapped[str] = mapped_column(String, ForeignKey('courses.id'))
    students_id: Mapped[str] = mapped_column(String, ForeignKey('students.id'))
    teachers_id: Mapped[str] = mapped_column(String, ForeignKey('teachers.id'))
    school_id: Mapped[str] = mapped_column(String, ForeignKey('schools.id'))  #
    grade: Mapped[int] = mapped_column(Integer)
