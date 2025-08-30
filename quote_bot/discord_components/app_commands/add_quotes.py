
import discord
from discord import app_commands


class ConfirmView(discord.ui.View):
    def __init__(self, exchange: str, context: str | None):
        super().__init__(timeout=None)  # or set a timeout in seconds
        self.exchange = exchange
        self.context = context

    @discord.ui.button(label="✅ Accept", style=discord.ButtonStyle.success)
    async def accept(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.edit_message(
            content=f"Quotes accepted:\n{self.exchange}"
            + (f" ({self.context})" if self.context else ""),
            view=None,  # removes the buttons after pressing
        )

    @discord.ui.button(label="✏️ Edit", style=discord.ButtonStyle.secondary)
    async def edit(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        # Re-open the modal for editing
        await interaction.response.send_modal(ExchangeModal(exchange=self.exchange, context=self.context))


class ExchangeModal(discord.ui.Modal, title="Add Quotes"):
    def __init__(self, exchange: str = "", context: str = ""):
        super().__init__(title="Add Quotes")

        # Build inputs dynamically, with defaults if provided
        self.exchange = discord.ui.TextInput(
            label="Quotes",
            style=discord.TextStyle.paragraph,
            placeholder='"Quote" - Speaker 1\n"Quote" - Speaker 2',
            required=True,
            default=exchange,
        )
        self.context = discord.ui.TextInput(
            label="Context",
            required=False,
            default=context,
        )

        self.add_item(self.exchange)
        self.add_item(self.context)


    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f'✅ Quotes stored:\n{self.exchange}'
            + (f" ({self.context})" if self.context.value else ""),
            view=ConfirmView(self.exchange.value, self.context.value),
            ephemeral=True,
        )


@app_commands.command(name="add_quotes", description="Add multiple quotes via form")
async def add_quotes(interaction: discord.Interaction) -> None:
    await interaction.response.send_modal(ExchangeModal())
