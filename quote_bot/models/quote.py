from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from quote_bot.models import Base, QuoteID, SpeakerID


class Quote(Base):
    __tablename__ = "quote"

    id: Mapped[QuoteID] = mapped_column(primary_key=True)
    """The ID of the quote entry"""
    content: Mapped[str]
    """The content of the quote"""
    context: Mapped[Optional[str]]
    """The context of the quote, if one is provided"""

    speaker_id: Mapped[SpeakerID] = mapped_column(ForeignKey("speaker.id"))
