# Discord.py Bot Template

Template project for building Discord bots in Python. Provides basic connection logic and a commands/events system using cogs.

## Project Structure

```
discord.py-template/
├── bot.py
├── requirements.txt
├── .env.example
├── .env
├── cogs/
│   ├── __init__.py
│   ├── events.py
│   └── server.py
```

## Cog Example

```python
import discord
from discord import app_commands
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Bot Latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000) if hasattr(self.bot, 'latency') else None
        if latency is None:
            await interaction.response.send_message("Latency information is unavailable.")
        else:
            await interaction.response.send_message(f"Pong! Latency: {latency}ms")

async def setup(bot):
    await bot.add_cog(Server(bot))
```