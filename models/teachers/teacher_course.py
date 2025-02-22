from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String, Integer, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.database import Base
from models.course import Course
from models.teachers.teacher import Teacher
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class TeacherCourse(Base, TimestampMixin):
    __tablename__ = "teacher_courses"
    teacher_id: Mapped[str] = mapped_column(Uuid, ForeignKey('teachers.id'))
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))

    course: Mapped['Course'] = relationship('Course', back_populates='student_courses')
    teacher: Mapped['Teacher'] = relationship('Teacher', back_populates='student_courses')