import Settings
from sources.Character import Character


class Game(object):
    characters = {}
    messages = []

    def __init__(self):
        pass

    def update(self, events, dt):
        self.messages = []

        for e in events:
            command = e.content.split(" ")
            if command[0] in self.commands:
                self.commands[command[0]](self, e)

        return self.messages

    def test(self, event):
        self.reply(event, "test")

    def create_character(self, event):
        self.characters[event.owner] = Character()
        self.reply(event, "created char")

    def get_hp(self, event):
        self.reply(event, str(self.characters[event.owner].hp))

    def help(self, event):
        self.reply(event, str(self.commands))

    def reply(self, event, content):
        self.send_message(event.raw_content.channel, content)

    def send_message(self, target, content):
        self.messages.append(Message(target, content))

    commands = {
        'test': test,
        'create_char': create_character,
        'help': help,
        'hp': get_hp,
    }


class Message(object):
    def __init__(self, target, content):
        self.target = target
        self.content = content

    def __repr__(self):
        return '<target: "' + self.target.name + '" content: "' + self.content + '">'
