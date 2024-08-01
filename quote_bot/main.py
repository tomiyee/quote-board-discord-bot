import os

from dotenv import load_dotenv

from quote_bot.discord_components.client import client

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    print("DISCORD_TOKEN is not set")
    exit(1)
client.run(DISCORD_TOKEN)
