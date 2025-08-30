import os

from dotenv import load_dotenv

# Import all models here to ensure they are registered with SQLAlchemy
from quote_bot import models  # noqa: F401
from quote_bot.database import Base, engine
from quote_bot.discord_components.client import client

load_dotenv()

# Initialize the database tables
Base.metadata.create_all(engine)

GUILD_ID = os.getenv("TESTING_GUILD_ID")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    print("DISCORD_TOKEN is not set")
    exit(1)
client.run(DISCORD_TOKEN)

"""
Remember to go to the Discord Developer Portal
(https://discord.com/developers/applications)
And make sure that OAuth2 -> URL Generator has the following scopes checked:
- bot
- applications.commands
And the following permissions (among others):
- Use Slash Commands
"""
