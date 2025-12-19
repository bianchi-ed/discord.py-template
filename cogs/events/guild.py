import discord
from discord.ext import commands

class GuildEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Joined guild: {guild.name} (id={guild.id})")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Removed from guild: {guild.name} (id={guild.id})")

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
    await bot.add_cog(GuildEvents(bot))
