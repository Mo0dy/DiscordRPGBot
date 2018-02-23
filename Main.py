import sources.DiscordIO as DiscordIO


# stores the messages written between iterations
events = []
DiscordIO.pass_event_list(events)


def main_loop():
    print("test")


DiscordIO.pass_main_loop(main_loop)


DiscordIO.launch_bot()
