import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def greet(ctx, arg):
    await ctx.send('Fuck you {0}'.format(arg))

@bot.command()
async def fiend(ctx):
    line = ""
    for i in range(10):
        line += '<:pussy_fiend:604532483626631168>'
    
    await ctx.send("looking for...me?")
    await ctx.send(line)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
        

bot.run('NjMxOTkwOTA5NDE1ODQ5OTg1.XZ_Z6w.A6YmSJbSHlt-xJEBPDJ4gweGGS8')
