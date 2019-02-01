import requests
import urllib
import discord
import os
from discord.ext.commands import Bot

image_directory = "C:/Users/kapihla/Pictures/Saved Pictures"

AUTH_TOKEN_FILE = open(".env", "r")
AUTH_TOKEN = str(AUTH_TOKEN_FILE.readlines(1)[0])
AUTH_TOKEN.replace("'", "")

MyBot = Bot(command_prefix=('$$'))



@MyBot.command(pass_context=True)
async def save_image(context, url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_directory + "/" + filename + ".jpg", 'wb') as image:
            image.write(response.content)
            await context.channel.send(content="Saved " + filename + ".")

@MyBot.command(pass_context=True)
async def load_image(context, filename):
    with open(image_directory + "/" + filename + ".jpg", 'rb') as image:
        await context.channel.send(content = "Here it is.")
        await context.channel.send(file = discord.File(image))


MyBot.run(AUTH_TOKEN)