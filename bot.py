import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=None, intents=intents)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue
        name = filename[:-3]
        try:
            await bot.load_extension(f'cogs.{name}')
            print(f"Loaded cog: {filename}")
        except Exception as e:
            print(f"Failed to load cog {filename}: {e}")
                
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await load_cogs()
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
