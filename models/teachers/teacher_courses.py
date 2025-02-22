from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String, Integer, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin

@genpareto_gen()
class Teachers(Base, TimestampMixin):
    __tablename__ = "teacher_courses"
    teacher_id: Mapped[str] = mapped_column(Uuid, ForeignKey('teachers.id'))
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))