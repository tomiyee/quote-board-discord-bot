from typing import Optional


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger


from quote_bot.database import Base


class Guild(Base):
    """Stores all information specific to an individual Guild"""

    __tablename__ = "guild"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    """Guild IDs are 64 bit integers, so we use BigInteger here"""

    quote_board_channel_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    """Channel IDs are also 64 bit integers. This is the channel where quotes will be posted."""
