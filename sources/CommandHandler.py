import discord
import asyncio
import sources.Game as Game
import Settings


class Request(object):
    def __init__(self, owner, content):
        self.owner = owner
        self.content = content


# coupling of reactions and functions (tasks)
class OnReaction(object):
    def __init__(self, message, emoji, action, user):
        self.message_id = message.id
        self.emoji = emoji
        self.action = action
        # the user that has to react
        self.user = user


class CommandHandler(object):
    def __init__(self, client, message_handler):
        self.client = client
        self.m_handler = message_handler
        self.requests = {}
        self.curr_request_id = 0
        self.game = None

        self.waiting_stack = []

    async def handle_command(self, message):
        await self.m_handler.send_targeted_message(message.author, message.channel, "handling command")
        # the string of the message without the command prefix
        command = message.content[len(Settings.command_prefix):]
        # the command separated into single blocks
        command = command.split(" ")
        # checks if command exists
        if command[0] in Game.commands:
            # calls the command associated with the string and assigns a request ID
            await Game.commands[command[0]](self.game, message.author, self.add_request(message.author, message))
        else:
            await self.m_handler.send_targeted_message(message.author, message.channel, "no such command")

    async def ask_question(self, target, channel, question, legend, option_labels, options):
        '''asks a questions and notes that it's waiting for a reply'''
        # prints question
        ask_str = question
        for i in range(len(option_labels)):
            ask_str += "\n" + option_labels[i] + " " + legend[i]
        send_message = await self.targeted_message(target, channel, ask_str)

        # add reactions (options)
        for i in range(len(option_labels)):
            await self.client.add_reaction(send_message, option_labels[i])
            # appends reactions to waiting stack also stores user that called the original command stored under the request_id
            self.waiting_stack.append(OnReaction(send_message, option_labels[i], options[i], target))

    async def handle_reaction(self, reaction, user):
        for w in self.waiting_stack:
            # the message id matches the one that the program is waiting for and the user is the correct
            if w.emoji == reaction.emoji and w.message_id == reaction.message.id and w.user == user:
                await w.action(self.game, user, self.add_request(user, reaction))
                self.waiting_stack.remove(w)

    async def targeted_message(self, target, channel, content):
        if type(content) != str:
            content = str(content)
        return await self.m_handler.send_targeted_message(target, channel, content)

    async def reply(self, request_id, content):
        if type(content) != str:
            content = str(content)
        request = self.get_request(request_id)
        return await self.m_handler.send_targeted_message(request.owner, self.get_channel(request_id), content)

    # request stuff
    def add_request(self, owner, content):
        self.requests[self.curr_request_id] = Request(owner, content)
        self.curr_request_id += 1
        return self.curr_request_id - 1

    def get_request(self, request_id):
        return self.requests[request_id]

    def get_owner(self, request_id):
        return self.requests[request_id].owner

    def get_content(self, request_id):
        return self.requests[request_id].content

    # gets channel from request
    def get_channel(self, request_id):
        request = self.get_request(request_id)
        if isinstance(request.content, discord.Message):
            return request.content.channel
        elif isinstance(request.content, discord.Reaction):
            return request.content.message.channel
