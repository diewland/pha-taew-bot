# This example requires the 'message_content' intent.

import os, re, random
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

words = [
    "เหงา",
    "ส่วนลด",
]
words_re = re.compile("|".join(words) ,re.IGNORECASE)

CODES = [
    "SSIS-440",
    "PRED-403",
    "IPX-258",
    "SHKD-772",
    "FSDSS-115",
    "STARS-157",
    "MEYD-540",
    "PPPD-807",
    "SSIS-195",
    "MEYD-605",
    "SSIS-260",
    "FSDSS-092",
    "IPX-750",
    "SW-331",
    "SCOP-707",
    "SSNI-984",
    "FSDSS-099",
    "IPX-597",
    "MIDE-715",
    "GENM-069",
    "IPX-293",
    "STARS-304",
    "YMDD-177",
    "SDAB-154",
    "IPX-581",
    "FSDSS-077",
    "GENM-060",
    "ATID-410",
    "MIAA-253",
    "MIFD-108",
    "SSNI-734",
    "SHN-018",
    "IPX-494",
    "SDJS-095",
    "FSDSS-079",
    "UMD-763",
    "SNIS-939",
    "SSNI-733",
    "MIDE-850",
    "SSNI-799",
    "IPX-091",
    "MIDE-570",
    "MEYD-642",
    "XVSR-060",
    "CSCT-004",
    "IMO-010",
    "SSNI-546",
    "ABW-023",
    "KMHRS-018",
    "FSDSS-014",
    "SDDE-606",
    "SSNI-569",
    "IPX-484",
    "HND-893",
    "SSNI-749",
    "CSCT-002",
    "JUFD-660",
    "IPX-451",
    "SDJS-098",
    "WAAA-013",
    "GENM-047",
    "FSDSS-019",
    "IPX-414",
    "CAWD-120",
    "SSNI-674",
    "MDTM-741",
    "IPX-586",
    "GENM-033",
    "DOCP-211",
    "MKMP-320",
    "SHKD-897",
    "FSDSS-026",
    "IPX-469",
    "CAWD-065",
    "SIM-067",
    "BF-605",
    "MEYD-583",
    "IPX-455",
    "MIDE-083",
    "ADN-243",
    "SSNI-751",
    "SHKD-898",
    "ABP-889",
    "SHKD-811",
    "RKI-605",
    "SSNI-746",
    "SHKD-836",
    "ABP-210",
    "MIDV-206",
    "MIAA-041",
    "SDJS-101",
    "BF-576",
    "HND-723",
    "ABW-295",
    "IPX-518",
    "REBDB-660",
    "MIMK-070",
    "PPPD-807",
    "MIDV-161",
    "ROYD-107",
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    # bot
    if message.author == client.user:
        return

    # detected
    elif words_re.search(message.content):
        mention = message.author.mention
        code = random.choice(CODES)
        await message.channel.send("{} คุณได้รับโค้ดส่วนลดจากช้อปปี้ `{}`".format(mention, code))

client.run(os.getenv('DISCORD_SHP'))
