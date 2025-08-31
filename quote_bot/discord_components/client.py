import os

import discord
from discord import app_commands
from dotenv import load_dotenv

from quote_bot.discord_components.app_commands.add_quote import add_quote
from quote_bot.discord_components.app_commands.get_board import get_board
from quote_bot.discord_components.app_commands.reset_board import reset_board
from quote_bot.discord_components.app_commands.set_board import set_board

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()

GUILD_ID = os.getenv("TESTING_GUILD_ID")


class QuoteBoardClient(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self) -> None:

        # Register all the commands on startup
        board_group = app_commands.Group(
            name="board", description="Commands related to the quote board"
        )
        board_group.add_command(get_board)
        board_group.add_command(set_board)
        board_group.add_command(reset_board)
        self.tree.add_command(board_group)
        self.tree.add_command(add_quote)

        print("All registered commands:")
        print("\t", list(map(lambda command: command.name, self.tree.get_commands())))

        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            await client.tree.sync(guild=guild)
            print(f"✅ Synced commands to guild {guild.id}")
        await self.tree.sync()
        print(f"We have logged in as {self.user}")


client = QuoteBoardClient()


@client.tree.command(name="ping", description="...")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("pong")
