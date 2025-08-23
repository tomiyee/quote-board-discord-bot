import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()

GUILD_ID = os.getenv("TESTING_GUILD_ID")


@client.event
async def on_ready() -> None:
    if GUILD_ID:
        guild = discord.Object(id=int(GUILD_ID))
        await client.tree.sync(guild=guild)
        print(f"✅ Synced commands to guild {GUILD_ID}")
    else:
        await client.tree.sync()
        print("🌍 Synced commands globally (may take up to 1 hour)")
    print(f"We have logged in as {client.user}")


class QuoteModal(discord.ui.Modal, title="Add Quote"):
    text = discord.ui.TextInput(
        label="Quote", style=discord.TextStyle.paragraph, required=True
    )
    speaker = discord.ui.TextInput(label="Speaker", required=True)
    context = discord.ui.TextInput(label="Context", required=False)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'✅ Quote stored:\n"{self.text}" — {self.speaker}'
            + (f" ({self.context})" if self.context.value else ""),
            ephemeral=True,
        )


@app_commands.command(name="add_quote", description="Add a quote via form")
async def add_quote(interaction: discord.Interaction):
    await interaction.response.send_modal(QuoteModal())


client.tree.add_command(add_quote)
