import Settings
from sources.Character import Character


class Game(object):
    characters = {}

    def __init__(self):
        pass

    def create_character(self, event):
        self.characters[event.owner] = Character()
