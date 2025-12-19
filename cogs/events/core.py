import discord
from discord.ext import commands

class CoreEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot ready: {self.bot.user}")

    @commands.Cog.listener()
    async def on_connect(self):
        print("Connected to gateway")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Disconnected from gateway")

async def setup(bot):
    await bot.add_cog(CoreEvents(bot))
