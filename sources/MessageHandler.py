import discord
import asyncio


class MessageHandler(object):
    def __init__(self, client):
        self.client = client

    async def send_message(self, target, content):
        return await self.client.send_message(target, content)

    async def reply(self, orig, content):
        return await self.send_message(orig.channel, ",\n===== " + orig.author.mention + " =====\n" + content + "\n=================")
