# This example requires the 'message_content' intent.

import os
import discord

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
        await message.channel.send("ป้ากำลังเตรียมร้านนะจ้า หน้าไม่งอรอไม่นานจ้า")

client.run(os.getenv('DISCORD_BOT'))
