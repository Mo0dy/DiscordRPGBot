import sources.DiscordIO as DiscordIO


# stores the messages written between iterations
events = []
DiscordIO.pass_event_list(events)
DiscordIO.launch_bot()
