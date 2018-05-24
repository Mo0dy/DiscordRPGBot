import discord
import asyncio


class MessageHandler(object):
    def __init__(self, client):
        self.client = client

    async def send_message(self, channel, content):
        return await self.client.send_message(channel, content)

    async def send_targeted_message(self, target, channel, content):
        return await self.send_message(channel,
                                       ",\n===== " + target.mention + " =====\n" + content + "\n=================")

