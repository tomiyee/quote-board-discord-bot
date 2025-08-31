import discord
from discord import app_commands
from sqlalchemy.orm import Session

from quote_bot.database import engine
from quote_bot.models.guild import Guild


@app_commands.command(name="reset", description="Delete the quote board setting")
async def reset_board(interaction: discord.Interaction) -> None:

    guild_id = interaction.guild.id if interaction.guild else None

    if not guild_id:
        await interaction.response.send_message(
            "Could not determine guild.", ephemeral=True
        )
        return

    with Session(engine) as session:
        guild = session.get(Guild, guild_id)

        if guild:
            guild.quote_board_channel_id = None
            session.commit()

    await interaction.response.send_message(
        "Cleared the quote board setting.",
        ephemeral=True,
    )
