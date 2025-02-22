import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, declarative_mixin, Mapped, mapped_column

@declarative_mixin
class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
