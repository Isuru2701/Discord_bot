import discord
from discord.ext import commands
import random
import pdb

intents = discord.Intents.all()
intents.members = True
Token = "OTIxMjI3NDU5MTU5MDE5NTYx.Ybv17Q.4kiqZ5FoGQ2nYWiu8mIxXirvwpk"
bot = commands.Bot(command_prefix=">", intents=intents)
status = ""


@bot.event
async def on_ready():

    print(f"\n {bot.user.name} ready")
    await bot.change_presence(activity=discord.Game(name="with thy mother"))


@bot.command(name="ping", help=" : check connection")
async def ping(ctx):
    print(f"{ctx.message.author} used {ctx.message.content}")
    await ctx.send(f'{round(bot.latency * 1000)}ms')


# @bot.command(name="anchor", help=": set to current channel") --might not need this
# async def read(ctx):

@bot.command(name="reply", help=': replies to your message  >reply <mention>')
async def reply(ctx, member: discord.Member = None):
    print(f"{ctx.message.author} used {ctx.message.content}")
    print(f'this is the value in member: {member}')

    if (member is None) or (member == ctx.message.author):
        await ctx.reply("Hello")
    else:
        await ctx.send(f"Hello {member.mention}")


@bot.command(name='say', help=': >say <text>')
async def say(ctx, *args):
    print(f"{ctx.message.author} used {ctx.message.content}")

    text = ""
    for i in args:
        text = text + " " + i
    await ctx.send(f'{text}')
    await ctx.message.delete()


@bot.command(name="make",
             help=": compiles story | syntax: >compile <starting message url>")
async def make(ctx, start: discord.Message):
    # pdb.set_trace()

    print(f"{ctx.message.author} used {ctx.message.content}")

    await ctx.send(f"**compiled**\n\ncompiling from <{start.jump_url}>, at {start.created_at}\n\n--------")

    messages = await start.channel.history(after=start, before=start.channel.last_message,
                                           oldest_first=True, limit=None).flatten()  # flatten converts to a list
    for message in messages:
        print(message.content)

    story = f"{start.content}"
    story_slices = []
    # while message != messages[-1]:
    #
    #     if len(story + message.content) >= 2000:
    #         await ctx.send(f"{story}")
    #         story = ""
    #         print("sent 1")
    #
    #         TODO if necessary
    #     # elif len(story + message.content) >= 4000:
    #     #     while :
    #     #     await ctx.send(f'{story[i:2000]}')
    #     #     if
    #
    #     story = story + " " + str(message.content)
    #     print(message.content)
    #
    #     i += 1
    #     message = messages[i]
    # else:
    #     await ctx.send(f"{story}")
    #     print(story)
    #     print(message.created_at != messages[-2].created_at)

    for message in messages:
        print(message.content)
        if message.content[0:2] != "||" and message.content[-2:] != "||":  # removes spoilers
            story = story + " " + message.content
    print("finished first for loop")

    if len(story) > 2000:
        while len(story) > 2000:
            story_slices.append(story[:2000])
            story = story[2000:]
            print(len(story))
    else:
        story_slices.append(story)
        print(len(story))
    print("finished while loop")

    for msg in story_slices:
        print(msg)
        await ctx.send(msg)
    print("finished final loop")
    print(len(messages))


@bot.command(name='spam', help='prints out random letters randomly | syntax: >spam <number of messages> ')
async def spam(ctx, amount: int):
    print(f"{ctx.message.author} used {ctx.message.content}")

    word = ""
    for i in range(0, amount):
        val = random.randint(1, 10)
        for j in range(0, val):
            word = word + chr(random.randint(65, 123))
        await ctx.send(word)
        word = ""
        print(i)


@bot.command(name="list", help="sends numbers in ascending order | syntax: >numbers <NO. numbers")
async def list(ctx, amount: int):
    for i in range(1, amount + 1):
        await ctx.send(i)
        print(i)

bot.run(Token)
