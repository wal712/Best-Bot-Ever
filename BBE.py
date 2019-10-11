import discord
import random

from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def greet(ctx, arg):
    await ctx.send('Fuck you {0}'.format(arg))

@bot.command()
async def fiend(ctx, *args):
    n = 10
    j = 10
    if len(args) == 1:
        n = int(args[0])
        j = int(args[0])
    elif len(args) >= 2:
        n = int(args[0])
        j = int(args[1])
        
    if n > 18 or n < 1:
        await ctx.send("yo chill")
    else:
        line = ""
        for i in range(n):
            line += '<:pussy_fiend:604532483626631168>'
        
        await ctx.send("looking for...me?")
        for i in range(j):
            await ctx.send(line)
            
@bot.command()
async def bak(ctx):
    await ctx.send(random.choice(['Bak Choi', 'Bak in Blak', 'Bak attack', 'Baby Bak Ribs']))
            
@bot.command()
async def business(ctx):
    await ctx.send("https://www.reddit.com/user/Business-Hacker/")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
        

bot.run('')
