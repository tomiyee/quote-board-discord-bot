from sqlalchemy import Column, ForeignKey, Integer, String

from quote_bot.database import Base


class Statement(Base):
    __tablename__ = "statements"

    id = Column(Integer, primary_key=True)
    speaker = Column(String, nullable=False)
    statement = Column(String, nullable=False)
    line_number = Column(Integer, nullable=False)
    exchange_id = Column(Integer, ForeignKey("exchanges.id"), nullable=False)
