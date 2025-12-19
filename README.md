# Discord.py Bot Template

Template project for building Discord bots in Python. Provides basic server connection logic and commands/events handling using cogs.

## Project Structure

```
discord.py-template/
├── bot.py                # Main
├── requirements.txt      
├── .env                  
├── cogs/                
│   ├── commands/         # Command cogs
│   │   └── server.py     
│   └── events/           # Event cogs
│       ├── core.py       
│       ├── message.py    
│       ├── member.py     
│       ├── guild.py      
│       ├── channel.py    
│       └── interaction.py 
```