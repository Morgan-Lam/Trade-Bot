import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
import mss
import time
#import requests

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
ChannelID = int(os.getenv("CHANNEL_ID"))
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class TradeBot():
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        bot = commands.Bot(command_prefix='!', intents=intents)
        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready():
                print(f"WE READY!!!!!, {self.client.user.name}")
                self.background_task()#CHANGE TO MSS
    
    async def notify(self, ID):
            channel = self.client.get_channel(ID)
            await channel.send("Trade Found")


    def TradeFound(self):
            asyncio.run_coroutine_threadsafe(self.notify(ChannelID),self.client.loop)

    def background_task(self):#CHANGE TO MSS and tesseract
        with mss.MSS() as sct:
            small_region = {'left': 0, 'top': 0, 'width': 100, 'height': 100}
            screenshot = sct.grab(small_region)
            print(screenshot)

            time.sleep(3)
            small_region2 = {'left': 0, 'top': 0, 'width': 100, 'height': 100}
            screenshot2 = sct.grab(small_region2)
            print(screenshot2)

        if screenshot != screenshot2:
            print("not =")
            self.TradeFound()

    def runBot(self):
        self.client.run(token, log_handler=handler, log_level=logging.DEBUG)

bot = TradeBot()
bot.runBot()


