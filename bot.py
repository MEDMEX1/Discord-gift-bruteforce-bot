import discord
from discord.ext import commands
import asyncio
import random as r
import string

#Gift bruteforce bot by MEDMEX

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("ready")



@client.command(pass_context=True)
async def start(ctx):
    var = 1
    while var == 1 :
        code = ''.join(r.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        channel = ctx.message.channel
        await channel.send("https://discord.gift/" + code)
        await asyncio.sleep(r.randint(2,5))


@client.command(pass_context=True)
async def test(ctx):
    channel = ctx.message.channel
    await client.send_message(channel, "https://discord.gift/" + "rhlRY2HnxMk2JDAK")

client.run(")
