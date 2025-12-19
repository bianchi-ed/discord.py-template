import discord
from discord.ext import commands

class InteractionEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        print(f"Interaction received: {interaction.type} by {getattr(interaction,'user',getattr(interaction,'author',None))}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"Command error: {error}")

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction, error):
        print(f"App command error: {error}")

async def setup(bot):
    await bot.add_cog(InteractionEvents(bot))
