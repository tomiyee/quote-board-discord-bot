from sqlalchemy import Column, Integer, String

from quote_bot.database import Base


class Exchange(Base):
    __tablename__ = "exchanges"

    id = Column(Integer, primary_key=True)  # arbitrary PK
    context = Column(String, nullable=True)  # nullable string
