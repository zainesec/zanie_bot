import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix='z>')

bot.run(TOKEN)
