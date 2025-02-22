import json

from sqlalchemy import Uuid, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.teachers.subject_specialities import SubjectSpecialties
from models.timestamp_mixin import TimestampMixin
from utils.repr_generator import generate_repr

@generate_repr()
class Teacher(Base, TimestampMixin):
    __tablename__ = "teachers"
    name: Mapped[str] = mapped_column(String(30))
    subject_specialties: Mapped[SubjectSpecialties] = mapped_column(Enum(SubjectSpecialties))
    grade_level: Mapped[int] = mapped_column(Integer)
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))

    teacher_courses: Mapped[list['TeacherCourse']] = relationship('TeacherCourse', back_populates='teacher')
