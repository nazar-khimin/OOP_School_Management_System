from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum

from models.base import Base

class SubjectSpecialties(Enum):
    MATH = "Math"
    SCIENCE = "Science"
    HISTORY = "History"
    LITERATURE = "Literature"
    ART = "Art"
    MUSIC = "Music"
    PHYSICAL_EDUCATION = "Physical Education"

class SubjectSpecialty(Base):
    __tablename__ = 'subject_specialties'
    name: Mapped[SubjectSpecialties] = mapped_column(SQLAlchemyEnum(SubjectSpecialties))