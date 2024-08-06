from sqlalchemy import Engine

# We need to import the SQLAlchemy models to add them to Base's metadata
from quote_bot.models import Base, quote, speaker  # noqa: F401


def sync_create_tables(engine: Engine) -> None:
    Base.metadata.create_all(engine)
