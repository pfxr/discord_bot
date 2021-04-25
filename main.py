import os
import discord
from commands import commands
from ytmusicapi import YTMusic

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.commands = commands.Commands('headers_auth.json')

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    async def on_message(self, message):
        print("Message received from "+str(message.author))
        print(message.content)

        if self.commands.check_prefix(message.content):
            msg_without_prefix = message.content[1:]
            if " " in msg_without_prefix:
                command, command_tail = msg_without_prefix.split(" ")
            else:
                command = msg_without_prefix
                command_tail = None

            print("Command " + command)
            if command_tail:
                print("Command Tail " + command_tail)

            func = getattr(self.commands, command, None)
            if not func:
                await message.channel.send(self.commands.command_not_found(None))
            else:
                await message.channel.send(func(command_tail))



b = Bot().run(os.getenv('DISCORD_TOKEN'))