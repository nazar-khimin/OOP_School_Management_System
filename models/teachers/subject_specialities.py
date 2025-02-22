from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

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
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[SubjectSpecialties] = mapped_column(Enum(SubjectSpecialties))
