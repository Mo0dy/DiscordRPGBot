from sources.Hero import Hero


class Session(object):
    ''' This saves the state of a user interaction with the game'''

    # the users hero
    hero = None

    def __init__(self):
        pass

    def new_hero(self):
        '''creates a new hero for the user'''
        self.hero = Hero()

    def get_hp(self):
        return self.hero.hp

    def get_attacked(self, damage):
        damage -= self.hero.stats["armor"]
        # armor subtracts from damage. Damage can never be less then one
        if damage < 1:
            damage = 1
        self.hero.hp -= damage
