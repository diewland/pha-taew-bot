# This example requires the 'message_content' intent.

import os, re
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

words = [ "เดร", "เ ด ร", " dre", " d r e", "dre ", "d r e " ]
words_re = re.compile("|".join(words) ,re.IGNORECASE)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    # bot
    if message.author == client.user:
        return

    # someone say "dre"
    elif words_re.search(message.content):
        mention = message.author.mention
        await message.channel.send("{} Dm me".format(mention))

client.run(os.getenv('DISCORD_DRE'))
