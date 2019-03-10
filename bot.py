import discord
from discord.ext import commands
import asyncio
import random
import string

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Genning nitro codes', type=0))
    print("ready")



@client.command(pass_context=True)
async def start(ctx):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    await client.send_message(ctx.message.channel, "https://discord.gift/" + code)
    return code


@client.command(pass_context=True)
async def test(ctx):
    channel = ctx.message.channel
    await client.send_message(channel, "https://discord.gift/" + "rhlRY2HnxMk2JDAK")
