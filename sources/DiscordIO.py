import discord
import asyncio
import Settings as Settings
import sources.Event as Event

client = discord.Client()


def pass_event_list(e):
    global events
    events = e


def pass_main_loop(m_l):
    global main_loop
    main_loop = m_l


def pass_messages(m):
    global messages
    messages = m


# adds the game main loop to the event list and runs it ten times a second
async def my_background_task():
    await client.wait_until_ready()
    while True:
        await asyncio.sleep(1 / Settings.loop_freq)
        main_loop()


async def messages_handler():
    await client.wait_until_ready()
    while True:
        # runs ten times a second
        await asyncio.sleep(1 / 10)
        for m in messages:
            await client.send_message(m.target, m.content)
        del messages[:]


def launch_bot():
    client.loop.create_task(my_background_task())
    client.loop.create_task(messages_handler())
    client.run("NDE2MjE5MTY4OTA4NjQwMjU2.DXBSFg.Dt_vYEiiA6F0YBHX7HQ4TvuDcU0")


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    if message.content.startswith(Settings.command_prefix):
        events.append(Event.Event(Event.MESSAGE, message.author.id,  message.content[len(Settings.command_prefix):], message))


@client.event
async def on_reaction_add(reaction, user):
    events.append(Event.Event(Event.REACTION, user.id, reaction.emoji, reaction))
