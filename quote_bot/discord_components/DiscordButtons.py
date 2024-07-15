from enum import Enum
from typing import Any

import discord
from discord import Interaction
from discord.ext import commands

from quote_bot.discord_components.client import client


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
