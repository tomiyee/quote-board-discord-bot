# This example requires the 'message_content' intent.
import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


print(os.environ["HOME"])

client.run(os.environ["DISCORD_TOKEN"])
