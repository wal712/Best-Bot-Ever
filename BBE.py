import discord
import random
import tensorflow as tf
import gpt_2_simple as gpt2
import os

from discord.ext import commands

bot = commands.Bot(command_prefix='$')


model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

file_name = "chatHistory.txt"
tf.reset_default_graph()
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
            file_name,
            model_name=model_name,
            steps=50)   # steps is max number of training steps

facts = ["During puberty, male penguins lose their beaks and grow a new one, much like humans lose their teeth", "There are 4 penguin embryos inside each  fertilized egg. However, there are not enough nutrients inside the egg to feed all 4. After these nutrients have been consumed the fetuses will attempt to consume one another. Only one will survive.", "Penguins enjoy eating ketchup. It is believed penguins are inherently polytheistic", "Most penguins are bisexual", "Penguins fucking suck", "Penguins have been observed becoming aroused when shown footage of the armenian genocide. The same cannot be said for footage of similar atrocities", "When placed in a room with nothing but cracker-jacks, a penguin will eat until it passes out.", "When placed in a room with nothing but diet dr. Pepper, penguins often reveal their zionist intentions.", "When placed in a room with nothing but analog clocks, a penguin will begin screaming", "Penguins will regurgitate a fish at least 200000 times before actually eating it.", "Penguins are staunch supporters of the blue lives matter movement.", "Contrary to popular belief, dancing as a penguin is punished by summarial execution.", "Penguins do not know how to drive.", "Penguins cannot swim in Snapple.", "Penguins choose not to swim in Snapple.", "Christopher Columbus's first officer aboard La Santa María was a penguin, who was tragically killed when the ship ran aground in Haiti in 1492.", "Penguins have 5 thumbs concealed under the feathers on each wing.", "Penguins are not 'legally' allowed to vote."]

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def greet(ctx, arg):
    await ctx.send('Fuck you {0}'.format(arg))
    
@bot.command()
async def update(ctx):
    txtfile = open("chatHistory.txt", "w", encoding="utf-8")
    
    # Gets list of past 1000 messages in chat
    messages = []
    async for message in ctx.history(limit = None):
        if  not message.author.bot and '$' not in message.content and 'http' not in message.content:
            messages.append(message.content)
    # Write history to text file
    txtfile.writelines(messages)
    
@bot.command()
async def textgen(ctx):
    text = gpt2.generate(sess, return_as_list=True, length = 100)
    await ctx.send(text[0])

    
    
    
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
async def roll(ctx, dice = 6, numRolls = 1):
    diceRange = int(dice)
    if diceRange < 1:
        await ctx.send("Invalid die value")
    else:
        rolls = int(numRolls)
        if rolls < 1 or rolls > 100:
            rolls = 1
        for i in range(numRolls):
            choice = random.choice(range(1, diceRange + 1))
            await ctx.send(choice)
            
@bot.command()
async def penguin(ctx):
    await ctx.send(random.choice(facts))     

@bot.command()
async def chat(ctx, length = 25):
    words = []
    async for message in ctx.history(limit = 1000):
        listwords = message.content.split()
        for word in listwords:
            words.append(word)
    await ctx.send(generate_markov_text(words, int(length)))
    
def database(words):
    cache = {}
    for w1, w2, w3 in triples(words):
        key = (w1, w2)
        if key in cache:
            cache[key].append(w3)
        else:
            cache[key] = [w3]  
    return cache

def generate_markov_text(words, size=25):
    cache = database(words)
    seed = random.randint(0, len(words)-3)
    seed_word, next_word = words[seed], words[seed+1]
    w1, w2 = seed_word, next_word
    gen_words = []
    for i in range(size):
        gen_words.append(w1)
        w1, w2 = w2, random.choice(cache[(w1, w2)])
    gen_words.append(w2)
    return ' '.join(gen_words)
    
def triples(words):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		
		if len(words) < 3:
			return
		
		for i in range(len(words) - 2):
			yield (words[i], words[i+1], words[i+2])     

@bot.command()
async def business(ctx):
    await ctx.send("https://www.reddit.com/user/Business-Hacker/")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
    
        

bot.run('NjMxOTkwOTA5NDE1ODQ5OTg1.XcXFuA.63LfiIt5HNhV2BQrBuhFExQyo6g')
