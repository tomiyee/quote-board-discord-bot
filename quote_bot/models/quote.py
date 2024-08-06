from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from quote_bot.models import Base, QuoteID, SpeakerID


class Quote(Base):
    __tablename__ = "quote"

    quote_id: Mapped[QuoteID] = mapped_column(primary_key=True)
    """The bot-assigned ID for this quote entry"""
    message_id: Mapped[int]
    """The Discord-assigned ID of the message the quote came from"""
    guild_id: Mapped[int]
    """The Discord-assigned ID of the message"""

    speaker_id: Mapped[SpeakerID] = mapped_column(ForeignKey("speaker.id"))
    """The speaker of the quote (not the author of the message)"""
    content: Mapped[str]
    """The content of the quote"""
    context: Mapped[Optional[str]]
    """The context of the quote, if one is provided"""
