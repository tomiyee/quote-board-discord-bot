from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from quote_bot.database import Base

# only for type hints
if TYPE_CHECKING:
    from quote_bot.models.exchange import Exchange


class Statement(Base):
    """An individiual statement said by a single person"""

    __tablename__ = "statement"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Unique ID of the Statement"""

    speaker: Mapped[str]
    statement: Mapped[str]
    line_number: Mapped[int]

    exchange_id: Mapped[int] = mapped_column(ForeignKey("exchange.id"), nullable=False)
    exchange: Mapped["Exchange"] = relationship(back_populates="statements")
