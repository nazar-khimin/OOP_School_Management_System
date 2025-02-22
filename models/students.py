from scipy.stats import genpareto_gen
from sqlalchemy import Uuid, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.timestamp_mixin import TimestampMixin

@genpareto_gen
class Students(Base, TimestampMixin):
    id: Mapped[int] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))