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
    await ctx.send("<:pussy_fiend:8>")
    # for i in range(10):
    #     line += ' :pussy_fiend: '
    
    # await ctx.send("looking for...me?")
    # for i in range(10):
    #     await ctx.send(line)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
        

bot.run('NjMxOTkwOTA5NDE1ODQ5OTg1.XZ_Vqw.fimpReqohBqskwrx40dvVX0_Q7A')
