# Discord.py Bot Template

A template for building Discord bots using `discord.py` with event and command handling via cogs.

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