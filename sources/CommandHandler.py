import discord
import asyncio


class CommandHandler(object):
    def __init__(self, client, message_handler):
        self.client = client
        self.m_handler = message_handler

    async def handle_command(self, command):
        await self.m_handler.reply(command, "handling command")

    async def handle_reaction(self, reaction, user):
        pass