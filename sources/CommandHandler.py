import discord
import asyncio
import sources.Game as Game
import Settings


class OnReaction(object):
    def __init__(self, message, emoji, action, request_id):
        self.message_id = message.id
        self.emoji = emoji
        self.action = action
        # the user that has to react
        self.request_id = request_id


class CommandHandler(object):
    def __init__(self, client, message_handler):
        self.client = client
        self.m_handler = message_handler
        self.requests = {}
        self.curr_request_id = 0
        self.game = None

        self.waiting_stack = []

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

    async def ask_question(self, request_id, question, legend, option_labels, options):
        '''asks a questions and notes that it's waiting for a reply'''
        # prints question
        ask_str = question
        for i in range(len(option_labels)):
            ask_str += "\n" + option_labels[i] + " " + legend[i]
        send_message = await self.reply(request_id, ask_str)

        # add reactions (options)
        for i in range(len(option_labels)):
            await self.client.add_reaction(send_message, option_labels[i])
            # appends reactions to waiting stack also stores user that called the original command stored under the request_id
            self.waiting_stack.append(OnReaction(send_message, option_labels[i], options[i], request_id))

    async def handle_reaction(self, reaction, user):
        print("reaction")
        print(self.waiting_stack)
        for w in self.waiting_stack:
            # the message id matches the one that the program is waiting for and the user is the correct
            if w.emoji == reaction.emoji and w.message_id == reaction.message.id and self.requests[w.request_id].author == user:
                print("found reaction")
                await w.action(self.game, user, w.request_id)

    async def reply(self, request_id, content):
        if type(content) != str:
            content = str(content)
        return await self.m_handler.reply(self.requests[request_id], content)

