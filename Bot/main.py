import os
import random
import asyncio
import discord
from discord.ext import commands
from config import TOKEN
from time import sleep

bot = commands.Bot(command_prefix='T!',
                   description='''Calling twitch into yours channel''')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    await bot.change_presence( status=discord.Status.offline)


def get_voiceline(champ):

  voicelines = os.listdir(champ)

  rvoice = random.choice(voicelines)
  return rvoice

@bot.command()
async def Twitch(ctx):

    try:
        channel = ctx.author.voice.channel
    except Exception:
        return await ctx.send("You must be in a voice channel")
    game = discord.Game("I was hiding")
    await bot.change_presence(activity=game, status=discord.Status.online)
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=os.path.abspath(f"Twitch/{get_voiceline('Twitch')}")))
    # Sleep while audio is playing.
    while vc.is_playing():
        sleep(.1)
    await vc.disconnect()
    await bot.change_presence(status=discord.Status.offline)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(bot.start(TOKEN))
except KeyboardInterrupt:
    loop.run_until_complete(bot.logout())
finally:
    loop.close()