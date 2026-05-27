import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
import mss





load_dotenv()
token = os.getenv("DISCORD_TOKEN")
ChannelID = int(os.getenv("CHANNEL_ID"))

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)


async def notify(ID):
        channel = client.get_channel(ID)
        await channel.send("Trade Found")


def TradeFound():
        asyncio.run_coroutine_threadsafe(notify(ChannelID),client.loop)

def background_task():
    print("Sending message from non-async thread...")
    TradeFound()


@client.event
async def on_ready():
        print(f"WE READY!!!!!, {client.user.name}")
        background_task()

client.run(token, log_handler=handler, log_level=logging.DEBUG)






