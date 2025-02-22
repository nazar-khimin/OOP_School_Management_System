from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class TeacherCourse(Base, TimestampMixin):
    __tablename__ = "teacher_courses"
    teacher_id: Mapped[str] = mapped_column(Uuid, ForeignKey('teachers.id'))
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))

    course: Mapped['Course'] = relationship('Course', back_populates='student_courses')
    teacher: Mapped['Teacher'] = relationship('Teacher', back_populates='student_courses')