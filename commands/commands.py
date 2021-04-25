from random import randrange
from ytmusicapi import YTMusic
import json


class Commands(YTMusic):
    def __init__(self, authentication):
        super().__init__(authentication)
        self.COMMAND_PREFIX = '!'

    def heads_or_tails(self, cmd_tail):
        if randrange(0, 2):
            return "heads"
        else:
            return "tails"

    def change_prefix(self, new_prefix):
        self.COMMAND_PREFIX = new_prefix
        return "New prefix is now " + new_prefix

    def search_music(self, song):
        results = self.search(song)
        for r in results:
            print(json.dumps(r, indent=4, sort_keys=True))
        return results[0]

    def play(self, song):
        print(self.get_streaming_data(song))

    def command_not_found(self, mock_param):
        return "Command not found"

    def check_prefix(self, msg):
        return msg[0] == self.COMMAND_PREFIX
