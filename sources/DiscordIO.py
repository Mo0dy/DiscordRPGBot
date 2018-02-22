import discord
import asyncio
import Settings as Settings
from sources.Event import Event

client = discord.Client()


def pass_event_list(e):
    global events
    events = e


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
    if message.content.startswith(Settings.command_prefix):
        message_no_prefix = message.content[len(Settings.command_prefix):]
        if message_no_prefix.split(" ")[0] in Settings.valid_commands:
            events.append(Event(message.author.id, message_no_prefix))
