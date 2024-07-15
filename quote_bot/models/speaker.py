from sqlalchemy.orm import Mapped, mapped_column

from quote_bot.models import Base, SpeakerID


class Speaker(Base):
    __tablename__ = "speaker"

    id: Mapped[SpeakerID] = mapped_column(primary_key=True)
    """The ID of the speaker entry"""
    guild: Mapped[str]
    """The guild id of the speaker."""
    name: Mapped[str]
    """The name of the speaker"""
