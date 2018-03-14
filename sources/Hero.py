import Settings


class Hero(object):
    inventory = ["pouch", "gold"]

    def __init__(self):
        self.hp = 100
        self.damage = 10
        self.stats = Settings.default_stats.copy()


