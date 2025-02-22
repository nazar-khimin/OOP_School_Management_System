from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class Student(Base, TimestampMixin):
    __tablename__ = "students"
    name: Mapped[str] = mapped_column(String(30))
    grade_level: Mapped[int] = mapped_column(Integer)
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))

    school: Mapped['School'] = relationship('Schools', back_populates='students')
    student_courses: Mapped[list['StudentCourse']] = relationship('StudentCourse', back_populates='student')