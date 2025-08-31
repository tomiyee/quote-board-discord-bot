import re
from datetime import date
from typing import Any

import discord
from discord import app_commands
from sqlalchemy.orm import Session

from quote_bot.database import engine
from quote_bot.models.guild import Guild


class ConfirmView(discord.ui.View):
    def __init__(self, exchange: str, context: str | None):
        super().__init__(timeout=None)  # or set a timeout in seconds
        self.exchange = exchange
        self.context = context

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success)
    async def accept(
        self, interaction: discord.Interaction, button: discord.ui.Button[Any]
    ) -> None:
        parsed_exchange = parse_quotes(self.exchange)
        formatted_exchange = format_quotes(parsed_exchange)
        context = self.context if self.context else "_No context_"

        await interaction.response.edit_message(
            content=f"Quote Preview:\n\n{formatted_exchange}\nContext: {context}\n",
            view=None,  # removes the buttons after pressing
        )

        # Look up the channel to post to
        guild_id = interaction.guild_id
        with Session(engine) as session:
            guild = session.get(Guild, guild_id)
            if guild is None or guild.quote_board_channel_id is None:
                return

        if interaction.guild is None:
            return

        quote_board = interaction.guild.get_channel(guild.quote_board_channel_id)

        if isinstance(quote_board, discord.TextChannel):
            await quote_board.send(f"{formatted_exchange}\nContext: {context}")

    @discord.ui.button(label="Edit", style=discord.ButtonStyle.secondary)
    async def edit(
        self, interaction: discord.Interaction, button: discord.ui.Button[Any]
    ) -> None:
        # Re-open the modal for editing
        await interaction.response.send_modal(
            ExchangeModal(exchange=self.exchange, context=self.context or "")
        )


class ExchangeModal(discord.ui.Modal, title="Add Quotes"):
    def __init__(self, exchange: str = "", context: str = ""):
        super().__init__(title="Add Quotes")

        today = date.today().strftime("%Y-%m-%d")

        # Build inputs dynamically, with defaults if provided
        self.date: discord.ui.TextInput["ExchangeModal"] = discord.ui.TextInput(
            label="Date (YYYY-MM-DD)",
            placeholder="YYYY-MM-DD",
            default=today,
        )

        # Build inputs dynamically, with defaults if provided
        self.exchange: discord.ui.TextInput["ExchangeModal"] = discord.ui.TextInput(
            label="Quotes",
            style=discord.TextStyle.paragraph,
            placeholder='"Quote" - Speaker 1\n"Quote" - Speaker 2',
            required=True,
            default=exchange,
        )
        self.context: discord.ui.TextInput["ExchangeModal"] = discord.ui.TextInput(
            label="Context",
            required=False,
            default=context,
        )

        self.add_item(self.date)
        self.add_item(self.exchange)
        self.add_item(self.context)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        parsed_exchange = parse_quotes(self.exchange.value)
        formatted_exchange = format_quotes(parsed_exchange)

        context = f"||{self.context.value}||" if self.context.value else "_No context_"
        await interaction.response.send_message(
            f"Quote Preview:\n\n{formatted_exchange}\nContext: {context}\n",
            view=ConfirmView(self.exchange.value, self.context.value),
            ephemeral=True,
        )


@app_commands.command(name="add_quotes", description="Add multiple quotes via form")
async def add_quotes(interaction: discord.Interaction) -> None:
    """
    Presents a modal dialog to the user to input multiple quotes and optional context.
    The user must confirm the quotes before they are accepted. They can edit them if the
    message was not parsed correctly or they want to make corrections
    """
    # Enforce that the command be used in a guild
    guild_id = interaction.guild_id
    if guild_id is None:
        await interaction.response.send_message(
            "This command can only be used in a server.", ephemeral=True
        )
        return

    # Look up the guild from the DB
    with Session(engine) as session:
        guild = session.get(Guild, guild_id)

    # If the guild is not in the DB or does not have a quote board channel set, stop
    if guild is None or guild.quote_board_channel_id is None:
        await interaction.response.send_message(
            "❌ This server does not have a quote board channel configured. "
            "Ask an admin to set one up before adding quotes.",
            ephemeral=True,
        )
        return

    await interaction.response.send_modal(ExchangeModal())


def parse_quotes(text: str) -> list[list[str]]:
    pattern = r'^"\s*(.*?)\s*"\s*-\s*(.*)$'
    result = []
    for line in text.strip().splitlines():
        match = re.match(pattern, line.strip())
        if match:
            quote, speaker = match.groups()
            result.append([quote, speaker])
    return result


def format_quotes(quotes: list[list[str]]) -> str:
    lines = []
    for quote, speaker in quotes:
        lines.append(f'"{quote}" - ||{speaker}||')
    return "\n".join(lines)
