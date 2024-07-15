import os

from dotenv import load_dotenv
from sqlalchemy import text

from quote_bot.database import engine
from quote_bot.discord_components.client import client

load_dotenv()


with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

if False:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    if DISCORD_TOKEN is None:
        print("DISCORD_TOKEN is not set")
        exit(1)
    client.run(DISCORD_TOKEN)
