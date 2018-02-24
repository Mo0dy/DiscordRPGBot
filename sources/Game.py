import Settings
from sources.Character import Character
from sources.CommandHandler import CommandHandler


class Game(object):
    characters = {}

    def __init__(self, command_handler):
        self.c_handler = command_handler

    def create_hero(self, session_id, request_id):
        self.characters[session_id] = Character()
        self.reply(request_id, "created character")

    def reply(self, request_id, content):
        self.c_handler.reply(request_id, content)


commands = {
    "create_hero": Game.create_hero
}