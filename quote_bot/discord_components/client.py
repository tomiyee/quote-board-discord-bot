from typing import Any

import discord
from discord.ext import commands

from quote_bot.parser import Parser

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.event
async def on_ready() -> None:
    print(f"We have logged in as {client.user}")


@client.command()
async def parse(ctx: commands.Context[Any]) -> None:
    """Parses the messages in the channel (and eventually save to a DB)

    Adds a reaction to indicate if parsing is successful.
    """
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=200):
        parsed_message = Parser.parse(message.content)
        # Use Reactions to indicate successfully parsing the quote
        await message.clear_reactions()
        await message.add_reaction("❌" if parsed_message is None else "✅")
        print(parsed_message)
