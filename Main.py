import sources.DiscordIO as DiscordIO
from sources.Game import Game

game = Game(DiscordIO.c_handler)

DiscordIO.launch_bot(game)
