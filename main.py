import discord
import logging
import logging.config
from dotenv import load_dotenv
from discord.ext import commands
import os

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix='z>')

@bot.event
async def on_ready():
    logger.info("The bot Is UP")

bot.run(TOKEN)
