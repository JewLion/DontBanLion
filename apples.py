import discord
from discord.ext import commands
import random
import asyncio
import urllib.request
import re

description = '''A bullshit bot made by Julian.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
@asyncio.coroutine
async def on_message(message):
	if message.content.startswith('feelsbadman.jpg'):
		await bot.send_message(message.channel, 'https://openclipart.org/image/2400px/svg_to_png/222252/feels.png')
		
	await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logging In')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello():
    """Says hello to the user."""
    await bot.say('Fuck You! I am a bot made by Julian. Type \'?help\' for a command list.')

@bot.command()
async def sub(left : int, right : int):
    """Subtracts two numbers together."""
    await bot.say(left - right)

@bot.command()
async def roll(dice : int):
		"""Rolls one dice"""
		result = random.randint(1,dice)
		await bot.say(str(result))

@bot.command()
async def oddsOn(num : int, action : str):
	"""OddsOn?"""
	odd1 = random.randint(1,num)
	odd2 = random.randint(1,num)

	if odd1 == odd2:
		await bot.say('You must ' + action)
	else:
		await bot.say('You got lucky')
	await bot.say('Roll 1: ' + str(odd1) + '\t\tRoll 2: ' + str(odd2))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times % 12):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def tags(command : str, query = 'query'):
    if command == 'list':
        """Lists all the commands"""
        msg = '```Tags:'
        for tag in list(sorted(bot.commands.keys())):
            msg += '\n\t' + tag
        msg += '```'
        await bot.say(msg)

    else:
        """Returns commands that fit the query"""
        msg = '```Tags found matching \'' + query + '\':'
        for tag in list(sorted(bot.commands.keys())):
            if tag.find(query) > -1:
                msg += '\n\t' + tag
        await bot.say(msg + '```')

@bot.command()
async def joke():
	"""It's a funny joke"""
	rand = random.randint(1,4)
	if rand == 1:
		await bot.say("What's got 5 arms, 3 legs, and 2 feet?")
		await bot.say('The Boston Marathon Finish Line!')
	elif rand == 2:
		await bot.say("Feminism.")
	elif rand == 3:
		await bot.say("Why do Jews have big noses?")
		await bot.say('Because air is free!')
	else:
		await bot.say("What is a redneck virgin?")
		await bot.say('A seven year old that can outrun her brothers!')

@bot.command()
async def randomow():
    """Picks a random Overwatch character"""
    charlist = ["Ana", "Bastion", "D.Va", "Genji", "Hanzo", "Junkrat", "Lucio", "McCree", "Mei", "Mercy", "Pharah", "Reaper", "Reinhardt", "Roadhoag", "Soldier: 76", "Symmetra", "Torbjorn", "Tracer", "Widowmaker", "Winston", "Zarya", "Zenyatta"]
    await bot.say(random.choice(charlist))
	
@bot.command()
async def wiki(query : str):
    """Returns the first Wikipedia result"""
    await bot.say('https://en.wikipedia.org/w/index.php?search=' + query.replace(" ", "+"))

@bot.command()
async def google(query : str):
    """Returns the Google search page"""
    await bot.say('https://www.google.com/search?num=100&site=webhp&source=hp&q=' + query.replace(" ", "+"))

@bot.command()
async def ytsearch(query:str):
	"""Returns the youtube search video"""
	await bot.say('https://www.youtube.com/results?search_query=' + query.replace(" ", "+"))

@bot.command()
async def youtube(query:str):
	"""Returns the first youtube video"""
	html_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query.replace(" ", "+")).read()
	matchObj = re.search( b'watch?', html_content, re.I|re.M)
	if matchObj:
		await bot.say(str(matchObj.group(0)))
	else:
		await bot.say('```No Video Found```')
		
@bot.command()
async def kys():
	await bot.say('https://s3.amazonaws.com/images.seroundtable.com/google-usa-suicide-1323868056.jpg')


@bot.command()
async def restart():
    await bot.say("``Restarting``")
    ##await self.disconnect_all_voice_clients()
    raise exceptions.RestartSignal

f = open("tokenLion.txt", "r")
bot.run(f.read())

