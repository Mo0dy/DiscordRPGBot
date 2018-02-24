import Settings
from sources.Character import Character


class Game(object):
    characters = {}

    def __init__(self, command_handler):
        self.c_handler = command_handler

    async def create_hero(self, session_id, request_id):
        self.characters[session_id] = Character()
        await self.reply(request_id, "created character")

    async def get_hp(self, session_id, request_id):
        await self.reply(request_id, self.get_session(session_id).hp)

    async def reply(self, request_id, content):
        if type(content) != str:
            content = str(content)
        await self.c_handler.reply(request_id, content)

    def get_session(self, session_id):
        return self.characters[session_id]

commands = {
    "new": Game.create_hero,
    "hp": Game.get_hp,
}