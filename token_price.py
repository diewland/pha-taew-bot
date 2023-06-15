import discord, os, sys, requests
from discord.ext import commands, tasks
#from datetime import datetime

# config from argv
(_, token, pair, env_name) = sys.argv

# init discord bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# get token price
def craft_status():
    #
    api = 'https://api1.binance.com/api/v3/avgPrice?symbol={}'.format(pair)
    #
    data = requests.get(api).json()
    price = data.get('price')
    status = f'{token} ${float(price):.4f}' if price is not None else '...'
    #return '{} at {}'.format(status, datetime.now().strftime('%H:%M:%S UTC+7'))
    return status

# create a task that changes the bot's status every 5 minutes
@tasks.loop(minutes=5)
async def change_status():
    status = craft_status()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

@change_status.before_loop
async def before_change_status():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # start the task
    change_status.start()

# run the bot
bot_token = os.getenv(env_name)
bot.run(bot_token)
