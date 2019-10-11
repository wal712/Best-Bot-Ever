import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))



bot.run('NjMxOTkwOTA5NDE1ODQ5OTg1.XZ_Gzw.yiFHzVVZGPMBYTMtVh6HGKZHxXI')
