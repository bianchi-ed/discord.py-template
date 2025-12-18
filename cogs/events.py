import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"Member joined: {member.name}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"Member left: {member.name}")

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        print(f"Role created: {role.name}")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        print(f"Role deleted: {role.name}")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        print(f"Role updated: {before.name} -> {after.name}")

async def setup(bot):
    await bot.add_cog(Events(bot))
