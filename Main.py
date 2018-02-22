import sources.DiscordIO as DiscordIO

DiscordIO.launch_bot()

# stores the messages written between iterations
events = []
DiscordIO.pass_event_list(events)
