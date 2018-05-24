import Settings
from sources.Session import Session
import discord


class Game(object):
    sessions = {}

    def __init__(self, command_handler):
        self.c_handler = command_handler

    async def create_hero(self, session_id, request_id):
        self.get_session(session_id).new_hero()
        await self.reply(request_id, "created character")

    async def get_hp(self, session_id, request_id):
        await self.reply(request_id, self.get_session(session_id).get_hp())

    # challenges another player to a duel
    async def challenge(self, session_id, request_id):
        mentions = self.c_handler.get_content(request_id).mentions
        # you can only challenge one person
        if len(mentions) == 1:
            opponent = mentions[0]
            # opponent is logged in
            if opponent in self.sessions:
                await self.ask_quest(opponent, self.c_handler.get_channel(request_id), "do you accept the challange?", ["yes", "no"], ["\N{grinning face}", "\N{face with tears of joy}"], [Game.fight, Game.pass_challange])
            else:
                await self.reply(request_id, (opponent.mention + "is not logged in"))
        else:
            await self.reply(request_id, "not enough mentions")

    async def fight(self, session_id, request_id):
        # the challanged person begins
        request = self.c_handler.get_request(request_id)
        pass

    async def pass_challange(self, session_id, request_id):
        await self.reply(request_id, "passed the challange")

    # creates and displays the main menu
    async def menu(self, session_id, request_id):
        request = self.c_handler.get_request(request_id)
        await self.ask_quest(request.owner, request.content.channel, "what menu point do you want?", ["hp", "create hero"], ["\N{grinning face}", "\N{face with tears of joy}"], [Game.get_hp, Game.create_hero])

    # asks a question with multiple options
    async def ask_quest(self, target, channel, content, legend, option_lables, options):
        await self.c_handler.ask_question(target, channel, content, legend, option_lables, options)

    # sends a message mentioning the author of the request
    async def reply(self, request_id, content):
        await self.c_handler.reply(request_id, content)

    # creates a session (the session stores current game state and the character)
    async def create_session(self, session_id, request_id):
        self.sessions[session_id] = Session()
        await self.reply(request_id, "created session")

    def get_session(self, session_id):
        return self.sessions[session_id]


    # just some fun xD
    async def cheer(self, session_id, request_id):
        await self.reply(request_id, "cheering!")
        await self.ask_quest(request_id, "do you want to cheer again?", ["cheer"],
                             ["\N{grinning face}"], [Game.cheer])


# this maps commands called in discord (i.e. ".new") to actual functions
commands = {
    "new": Game.create_hero,
    "hp": Game.get_hp,
    "login": Game.create_session,
    "menu": Game.menu,
    "cheer": Game.cheer,
    "challenge": Game.challenge,
}
