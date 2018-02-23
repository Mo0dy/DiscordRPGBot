import sources.DiscordIO as DiscordIO
from sources.Game import Game
import time


# some not game related settings
debug = True


# stores the messages written between iterations
events = []
DiscordIO.pass_event_list(events)

# create new game
game = Game()

last_time = time.time()
def main_loop():
    global events, last_time
    # calculate dt
    curr_time = time.time()
    dt = curr_time - last_time
    last_time = curr_time

    if debug:
        printed = False
        for e in events:
            print(e)
            printed = True
        if printed:
            print("")

    # update game
    game.update(events, dt)

    # be careful not to change the reference
    del events[:]


DiscordIO.pass_main_loop(main_loop)


DiscordIO.launch_bot()
