"""
Explicit imports of all the model definitions to ensure they are registered with
SQLAlchemy.
"""

from quote_bot.models.exchange import Exchange  # noqa: F401
from quote_bot.models.guild import Guild  # noqa: F401
from quote_bot.models.statement import Statement  # noqa: F401
