import Settings
from sources.Character import Character


class Game(object):
    characters = {}

    def __init__(self, command_handler):
        self.c_handler = command_handler

    async def create_hero(self, session_id, request_id):
        self.characters[session_id] = Character()
        await self.reply(request_id, "created character")

    async def reply(self, request_id, content):
        await self.c_handler.reply(request_id, content)


commands = {
    "create_hero": Game.create_hero
}