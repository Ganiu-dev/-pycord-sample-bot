import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    """A simple plugin that responds to a slash command."""
    
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check if the ExpandoBot plugin system is working.")
    async def ping(self, interaction: discord.Interaction):
        # Create a nice embed response
        embed = discord.Embed(
            title="Pong!",
            description="The ExpandoBot plugin system works perfectly.",
            color=discord.Color.brand_green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    """This is the required entry point for py-cord to load the plugin."""
    await bot.add_cog(Ping(bot))
