from tokenize import String

from sqlalchemy import Uuid
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin
from repr.repr_generator import generate_repr

@generate_repr()
class School(Base, TimestampMixin):
    __tablename__ = "schools"
    id: Mapped[int] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String)
