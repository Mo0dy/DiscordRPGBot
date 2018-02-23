

MESSAGE = 1
REACTION = 2


class Event(object):
    def __init__(self, e_type, owner, content, raw_content):
        self.type = e_type
        self.owner = owner
        self.content = content
        self.raw_content = raw_content

    def __repr__(self):
        e_type = "unknown type"
        # this should be done as a data structure
        if self.type == MESSAGE:
            e_type = "message"
        elif self.type == REACTION:
            e_type = "reaction"

        return '<Event: "' + e_type + '" owner: "' + self.owner + '" content: "' + self.content + '">'
