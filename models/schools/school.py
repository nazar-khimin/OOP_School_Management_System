from sqlalchemy import Uuid, String
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class Schools(Base, TimestampMixin):
    __tablename__ = "schools"
    name: Mapped[str] = mapped_column(String(30))