import discord
import asyncio
import Settings as Settings

client = discord.Client()


def launch_bot():
    client.run("NDE2MjE5MTY4OTA4NjQwMjU2.DXBSFg.Dt_vYEiiA6F0YBHX7HQ4TvuDcU0")


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    if(message.content.startswith(Settings.command_prefix)):
        print(message.content)
