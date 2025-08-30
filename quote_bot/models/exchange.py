from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship

from quote_bot.database import Base

# only for type hints
if TYPE_CHECKING:
    from quote_bot.models.statement import Statement


class Exchange(Base):
    """An exchange is a collection of statements and data associated with the group"""

    __tablename__ = "exchange"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Unique ID of the exchange"""

    context: Mapped[Optional[str]]
    """The context or topic of the exchange"""

    statements: Mapped[List["Statement"]] = relationship(
        back_populates="exchange", cascade="all, delete-orphan"
    )
