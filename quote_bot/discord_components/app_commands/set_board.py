import discord
from discord import app_commands
from sqlalchemy.orm import Session

from quote_bot.database import engine
from quote_bot.models.guild import Guild


@app_commands.command(
    name="set_board", description="Set the current text channel as the quote board"
)
async def set_board(interaction: discord.Interaction) -> None:

    guild_id = interaction.guild.id if interaction.guild else None
    channel_id = interaction.channel.id if interaction.channel else None

    if not guild_id or not channel_id:
        await interaction.response.send_message(
            "Could not determine guild or channel.", ephemeral=True
        )
        return

    with Session(engine) as session:
        guild = session.query(Guild).filter_by(id=guild_id).first()
        if guild:
            guild.quote_board_channel_id = channel_id
        else:
            guild = Guild(id=guild_id, quote_board_channel_id=channel_id)
            session.add(guild)
        session.commit()

    await interaction.response.send_message(
        f"✅ Set <#{channel_id}> as the quote board channel for this server.",
        ephemeral=True,
    )
