import discord
from discord.ext import commands

class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"Member joined: {member.name}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"Member left: {member.name}")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        print(f"Member updated: {getattr(before, 'id', None)}")

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        print(f"User updated: {getattr(before, 'id', None)}")

async def setup(bot):
    await bot.add_cog(MemberEvents(bot))
