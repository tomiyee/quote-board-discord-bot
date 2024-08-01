# This example requires the 'message_content' intent.
import os
from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional

import discord
from discord import Interaction
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.event
async def on_ready() -> None:
    print(f"We have logged in as {client.user}")


class Person(Enum):
    TOMMY = "Tommy"
    KAYLEE = "Kaylee"
    SERGIO = "Sergio"
    ANDREA = "Andrea"


class Buttons(discord.ui.View):

    def __init__(self, answer: Person, timeout: int = 180) -> None:
        super().__init__(timeout=timeout)
        self.answer = answer

    @discord.ui.button(label="Tommy", style=discord.ButtonStyle.gray)
    async def tommy_button(
        self, interaction: Interaction, b: discord.ui.Button[Any]
    ) -> None:
        await interaction.response.edit_message(
            content="Correct!" if self.answer == Person.TOMMY else "Incorrect!",
            view=self,
        )

    @discord.ui.button(label="Kaylee", style=discord.ButtonStyle.gray)
    async def kaylee_button(
        self, interaction: Interaction[Any], b: discord.ui.Button[Any]
    ) -> None:
        await interaction.response.edit_message(
            content="Correct!" if self.answer == Person.KAYLEE else "Incorrect!",
            view=self,
        )

    @discord.ui.button(label="Sergio", style=discord.ButtonStyle.gray)
    async def sergio_button(
        self, interaction: Interaction, b: discord.ui.Button[Any]
    ) -> None:
        await interaction.response.edit_message(
            content="Correct!" if self.answer == Person.SERGIO else "Incorrect!",
            view=self,
        )

    @discord.ui.button(label="Andrea", style=discord.ButtonStyle.gray)
    async def andrea_button(
        self, interaction: Interaction, b: discord.ui.Button[Any]
    ) -> None:
        await interaction.response.edit_message(
            content="Correct!" if self.answer == Person.ANDREA else "Incorrect!",
            view=self,
        )


@client.command()
async def guess(ctx: commands.Context[Any]) -> None:
    quote = "So I split the big ol titty in half"
    await ctx.send(
        f"Who said this quote! \n\n> {quote}\n",
        view=Buttons(
            answer=Person.ANDREA,
        ),
    )


@client.command()
async def parse(ctx: commands.Context[Any]) -> None:
    """Parses the messages in the channel (and eventually save to a DB)"""
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=200):
        parsed_message = parse_message(message.content)
        # Use Reactions to indicate successfully parsing the quote
        await message.add_reaction("\uF44E" if parsed_message is None else "\uF44D")
        print(parse_message(message.content))
        print("Message ID", message.id)
        print("Channel ID", message.channel.id)


@dataclass
class ParsedMessage:
    """The results of parsing the content of a quote-board message"""

    quote: str
    """The content of the quote"""
    speaker: str
    """The name of the one who spoke the quote"""
    context: str | None
    """(optional) Any context accompanying the quote"""


def parse_message(content: str) -> Optional[ParsedMessage]:
    return None
    # return ParsedMessage()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    print("DISCORD_TOKEN is not set")
    exit(1)
client.run(DISCORD_TOKEN)
