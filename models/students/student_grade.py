from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class StudentGrade(Base, TimestampMixin):
    __tablename__ = "student_grades"
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))
    students_id: Mapped[str] = mapped_column(Uuid, ForeignKey('students.id'))
    teachers_id: Mapped[str] = mapped_column(Uuid, ForeignKey('teachers.id'))
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))    #
    grade: Mapped[int] = mapped_column(Integer)