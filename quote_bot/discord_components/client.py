from enum import Enum
from typing import Any

import discord
from discord.ext import commands
from sqlalchemy import select
from sqlalchemy.orm import Session

from quote_bot.database import engine
from quote_bot.models.speaker import Speaker
from quote_bot.parser import ParsedMessage, Parser

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


class React(Enum):
    """An enum for all of the emojis and what they represent"""

    SAVED = "📋"
    """The quote has been successfully saved to the DB"""
    PARSED = "✅"
    """The quote has been successfully parsed into quote, speaker, and context"""
    FAILED_PARSE = "❌"
    """The quote was unable to be clearly parsed"""
    FAILED_SPEAKER = "🚷"
    """The speaker did not match a name seen before"""


@client.event
async def on_ready() -> None:
    print(f"We have logged in as {client.user}")


@client.command()
async def parse(ctx: commands.Context[Any]) -> None:
    """Parses the messages in the channel (and eventually save to a DB)

    Adds a reaction to indicate if parsing is successful.
    """
    await ctx.message.delete()
    new_parsed_messages: list[tuple[ParsedMessage, discord.Message]] = []
    async for message in ctx.channel.history(limit=200):
        # skip messages that were successfully parsed
        already_parsed = any(
            react.emoji == React.PARSED.value and react.me
            for react in message.reactions
        )
        if already_parsed:
            continue
        # Use Reactions to indicate successfully parsing the quote
        parsed_message = Parser.parse(message.content)
        await message.clear_reactions()
        await message.add_reaction(
            React.FAILED_PARSE.value if parsed_message is None else React.PARSED.value
        )
        if parsed_message is not None:
            new_parsed_messages.append((parsed_message, message))

    with Session(engine) as session:
        for parsed_message, message in new_parsed_messages:

            matching_speaker = (
                select(Speaker).where(Speaker.name.is_(parsed_message.speaker)).limit(1)
            )

            speaker = session.scalar(matching_speaker)

            if speaker is None:
                await message.add_reaction(React.FAILED_SPEAKER.value)
