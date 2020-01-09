import discord, asyncio
from os import system
import shutil
import subprocess

client = discord.Client()

token = ""

def owo(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("owo".center(width))
        print()
        print("[-] Developed by micah [-]".center(width))
        print("[-] User: {0} [-]".format(client.user).center(width))
        print()
    ui()
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == 'cl':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'cleardms':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

client.run(token, bot=False)
