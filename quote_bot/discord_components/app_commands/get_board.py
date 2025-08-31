import discord
from discord import app_commands
from sqlalchemy.orm import Session

from quote_bot.database import engine
from quote_bot.models.guild import Guild


@app_commands.command(name="get_board", description="Get the current board")
async def get_board(interaction: discord.Interaction) -> None:

    guild_id = interaction.guild.id if interaction.guild else None

    if not guild_id:
        await interaction.response.send_message(
            "Could not determine guild.", ephemeral=True
        )
        return

    with Session(engine) as session:
        guild = session.get(Guild, guild_id)

    if guild is None or guild.quote_board_channel_id is None:
        await interaction.response.send_message(
            "This server does not have a text chat set as the quote board",
            ephemeral=True,
        )
        return

    await interaction.response.send_message(
        f"The current quote board for the server is <#{guild.quote_board_channel_id}>.",
        ephemeral=True,
    )
