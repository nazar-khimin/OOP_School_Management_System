from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.database import Base
from models.course import Course
from models.students.student import Student
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class StudentCourse(Base, TimestampMixin):
    __tablename__ = "student_courses"
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))
    students_id: Mapped[str] = mapped_column(Uuid, ForeignKey('students.id'))


    course: Mapped['Course'] = relationship('Course', back_populates='student_courses')
    student: Mapped['Student'] = relationship('Student', back_populates='student_courses')