# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    # Respond to "$hello" with "Hello!""
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    print("DISCORD_TOKEN is not set")
    exit(1)
client.run(DISCORD_TOKEN)
