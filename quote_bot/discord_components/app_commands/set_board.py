import discord
from discord import app_commands

@app_commands.command(name="set_board", description="Set the current text channel as the quote board")
async def set_board(interaction: discord.Interaction) -> None:
  
  with Session(engine) as session:
    session.commit()
    pass
