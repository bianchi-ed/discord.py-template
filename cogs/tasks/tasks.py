import discord
from discord.ext import commands, tasks

class ExampleTask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.example_task.start()

    def cog_unload(self):
        self.example_task.cancel()

    @tasks.loop(minutes=60)
    async def example_task(self):
        print("Example task activated.")

    @example_task.before_loop
    async def before_example_task(self):
        print("Waiting for bot to be ready.")
        await self.bot.wait_until_ready()
        
async def setup(bot):
    await bot.add_cog(ExampleTask(bot))