import sources.DiscordIO as DiscordIO


# stores the messages written between iterations
events = []
DiscordIO.pass_event_list(events)


def main_loop():
    global events
    printed = False
    for e in events:
        print(e)
        printed = True
    if printed:
        print("")
    # be careful not to change the reference
    del events[:]


DiscordIO.pass_main_loop(main_loop)


DiscordIO.launch_bot()
