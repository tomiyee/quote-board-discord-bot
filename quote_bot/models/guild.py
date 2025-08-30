from sqlalchemy import Column, Integer, String

from quote_bot.database import Base


class Guild(Base):
    """Stores all information specific to an individual Guild"""

    __tablename__ = "guild"

    id = Column(Integer, primary_key=True)
    """Guild ID"""

    quote_board_channel = Column(String)
    """The channel ID of the quote board channel"""
