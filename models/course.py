from sqlalchemy import String, Uuid, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from models.schools.school_course import SchoolCourse
from models.students.student_course import StudentCourse
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class Course(Base, TimestampMixin):
    __tablename__ = 'courses'
    name: Mapped[str] = mapped_column(String(30))
    teacher_id: Mapped[str] = mapped_column(Uuid, ForeignKey('teachers.id'))
    max_capacity: Mapped[int] = mapped_column(Integer)
    required_grade_level: Mapped[int] = mapped_column(Integer)
    credits: Mapped[int] = mapped_column(Integer)

    school_courses: Mapped[list['SchoolCourse']] = relationship('SchoolCourse', back_populates='course')
    student_courses: Mapped[list['StudentCourse']] = relationship('StudentCourse', back_populates='course')