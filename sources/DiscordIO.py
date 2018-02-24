import discord
import asyncio
import Settings as Settings
from sources.CommandHandler import CommandHandler
from sources.MessageHandler import MessageHandler


client = discord.Client()
m_handler = MessageHandler(client)
c_handler = CommandHandler(client, m_handler)


def launch_bot(game):
    c_handler.game = game
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
        await c_handler.handle_command(message)


@client.event
async def on_reaction_add(reaction, user):
    await c_handler.handle_reaction(reaction, user)
