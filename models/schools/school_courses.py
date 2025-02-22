from sqlalchemy import Uuid, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class SchoolCourses(Base, TimestampMixin):
    __tablename__ = "school_courses"
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))
    course_id: Mapped[str] = mapped_column(Uuid, ForeignKey('courses.id'))


    school: Mapped['Schools'] = relationship('Schools', back_populates='students')
