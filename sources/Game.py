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

    async def menu(self, session_id, request_id):
        await self.ask_quest(request_id, "what menu point do you want?", ["hp", "create hero"], ["\N{grinning face}", "\N{face with tears of joy}"], [self.get_hp, self.create_hero])

    async def ask_quest(self, request_id, content, legend, option_lables, options):
        await self.c_handler.ask_question(request_id, content, legend, option_lables, options)

    async def reply(self, request_id, content):
        await self.c_handler.reply(request_id, content)

    async def create_session(self, session_id, request_id):
        self.sessions[session_id] = Session()
        await self.reply(request_id, "created session")

    def get_session(self, session_id):
        return self.sessions[session_id]


commands = {
    "new": Game.create_hero,
    "hp": Game.get_hp,
    "login": Game.create_session,
    "menu": Game.menu,
}
