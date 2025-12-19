import discord
from discord.ext import commands

class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        print(f"Message edited: id={getattr(after,'id',None)} by {getattr(after,'author',None)}")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(f"Message deleted: id={getattr(message,'id',None)} from {getattr(message,'author',None)}")

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        print(f"Bulk message delete: count={len(messages)}")

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        print(f"Typing: {user} in {getattr(channel, 'name', channel)} at {when}")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(f"Reaction added: {reaction} by {user}")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        print(f"Reaction removed: {reaction} by {user}")

async def setup(bot):
    await bot.add_cog(MessageEvents(bot))
