from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin

@genpareto_gen
class Students(Base, TimestampMixin):
    name: Mapped[str] = mapped_column(String(30))
    grade_level: Mapped[int] = mapped_column(Integer)
    school_id: Mapped[str] = mapped_column(Uuid, ForeignKey('schools.id'))