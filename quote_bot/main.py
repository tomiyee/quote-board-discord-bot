import os

from dotenv import load_dotenv

from quote_bot.discord_components.client import client

# from quote_bot.database import engine
# from sqlalchemy import text


load_dotenv(override=True)


# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    print("DISCORD_TOKEN is not set")
    exit(1)
client.run(DISCORD_TOKEN)
