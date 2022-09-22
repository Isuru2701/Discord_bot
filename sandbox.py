import discord
from discord.ext import commands
import random
import pdb

intents = discord.Intents.all()
intents.members = True
Token = "OTIxMjI3NDU5MTU5MDE5NTYx.Ybv17Q.4kiqZ5FoGQ2nYWiu8mIxXirvwpk" #obtain token from going to ur discord API
bot = commands.Bot(command_prefix="&", intents=intents)
status = ""

@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(activity = discord.Game(name = "yuis"))


@bot.command(name="ping", help=" : check connection")
async def ping(ctx):
    print(f"{ctx.message.author} used {ctx.message.content}")
    await ctx.send(f'{round(bot.latency * 1000)}ms')


bot.run(Token)
