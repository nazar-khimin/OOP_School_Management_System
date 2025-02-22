from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String, Integer, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.database import Base
from models.teachers.teacher_course import TeacherCourse
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class Teacher(Base, TimestampMixin):
    __tablename__ = "teachers"
    name: Mapped[str] = mapped_column(String(30))
    subject_specialties: Mapped[list] = mapped_column(ARRAY(String))
    grade_level: Mapped[int] = mapped_column(Integer)
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))

    teacher_courses: Mapped[list['TeacherCourse']] = relationship('TeacherCourse', back_populates='teacher')