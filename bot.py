# This example requires the 'message_content' intent.

import os, discord
from menu import gen_msg

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    # bot
    if message.author == client.user:
        return

    # conditions
    mentioned = client.user.mentioned_in(message)
    hungry = message.content.find('หิว') > -1
    not_hungry = message.content.find('ไม่หิว') > -1

    # skip: not hungry
    if not_hungry:
        pass

    # detect hungry
    elif mentioned or hungry:
        mention = message.author.mention
        msg = gen_msg()
        await message.channel.send("{} {}".format(mention, msg))

client.run(os.getenv('DISCORD_BOT'))
