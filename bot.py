# This example requires the 'message_content' intent.

import os, discord
from menu import gen_msg

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        msg = gen_msg()
        await message.channel.send(msg)

client.run(os.getenv('DISCORD_BOT'))
