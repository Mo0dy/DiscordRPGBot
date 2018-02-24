import discord
import asyncio
import sources.Game as Game
import Settings


class CommandHandler(object):
    def __init__(self, client, message_handler):
        self.client = client
        self.m_handler = message_handler
        self.requests = {}
        self.curr_request_id = 0
        self.game = None

    async def handle_command(self, message):
        await self.m_handler.reply(message, "handling command")
        # the string of the message without the command prefix
        command = message.content[len(Settings.command_prefix):]
        # the command separated into single blocks
        command = command.split(" ")
        # checks if command exists
        if command[0] in Game.commands:
            # calls the command associated with the string and assigns a request ID
            await Game.commands[command[0]](self.game, message.author, self.add_request(message))
        else:
            await self.m_handler.reply(message, "no such command")

    def add_request(self, message):
        self.requests[self.curr_request_id] = message
        self.curr_request_id += 1
        return self.curr_request_id - 1

    async def handle_reaction(self, reaction, user):
        pass

    async def reply(self, request_id, content):
        await self.m_handler.reply(self.requests[request_id], content)
