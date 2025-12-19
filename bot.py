import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)

async def _noop_process_commands(message):
    return

bot.process_commands = _noop_process_commands

async def load_cogs():
    try:
        from cogs import EXTENSIONS
        for ext in EXTENSIONS:
            try:
                await bot.load_extension(ext)
                print(f"Loaded cog: {ext}")
            except Exception as e:
                print(f"Failed to load cog {ext}: {e}")
        return
    except Exception:
        pass

        base = os.path.abspath('./cogs')
        modules = []
        for root, _, files in os.walk(base):
            for filename in sorted(files):
                if not filename.endswith('.py'):
                    continue
                if filename == '__init__.py' or filename.startswith('_'):
                    continue
                filepath = os.path.join(root, filename)
                rel = os.path.relpath(filepath, base)
                module = os.path.splitext(rel)[0].replace(os.sep, '.')
                full = f'cogs.{module}'
                modules.append(full)

        # Load in deterministic order
        for full in sorted(set(modules)):
            try:
                await bot.load_extension(full)
                print(f"Loaded cog: {full}")
            except Exception as e:
                print(f"Failed to load cog {full}: {e}")
                
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
