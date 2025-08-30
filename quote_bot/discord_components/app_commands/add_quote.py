import discord
from discord import app_commands


class QuoteModal(discord.ui.Modal, title="Add Quote"):
    text: discord.ui.TextInput["QuoteModal"] = discord.ui.TextInput(
        label="Quote", required=True, style=discord.TextStyle.paragraph
    )
    speaker: discord.ui.TextInput["QuoteModal"] = discord.ui.TextInput(
        label="Speaker", required=True
    )
    context: discord.ui.TextInput["QuoteModal"] = discord.ui.TextInput(
        label="Context", required=False
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f'✅ Quote stored:\n"{self.text}" — {self.speaker}'
            + (f" ({self.context})" if self.context.value else ""),
            ephemeral=True,
        )


@app_commands.command(name="add_quote", description="Add a quote via form")
async def add_quote(interaction: discord.Interaction) -> None:
    await interaction.response.send_modal(QuoteModal())
