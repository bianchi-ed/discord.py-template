import discord
from discord.ext import commands

class ChannelEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        print(f"Channel created: {getattr(channel,'name',channel)} (id={getattr(channel,'id',None)})")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        print(f"Channel deleted: {getattr(channel,'name',channel)}")

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        print(f"Channel updated: {getattr(before,'name',before)} -> {getattr(after,'name',after)}")

    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        parent = getattr(thread, 'parent', None)
        print(f"Thread created: {getattr(thread,'name',thread)} in {getattr(parent,'name',parent)}")

    @commands.Cog.listener()
    async def on_thread_update(self, before, after):
        print(f"Thread updated: {getattr(after,'id',None)}")

    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        print(f"Thread deleted: {getattr(thread,'id',None)}")

async def setup(bot):
    await bot.add_cog(ChannelEvents(bot))
