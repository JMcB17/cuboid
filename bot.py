#!/usr/bin/env python

import json
import argparse
from pathlib import Path

import discord.ext.commands


__version__ = '0.1.0'


CONFIG_PATH = Path('config.json')


class CuboidBot(discord.ext.commands.Bot):
    def __init__(self, config, *args, **kwargs):
        self.config = config

        parser = argparse.ArgumentParser()
        self.parser = parser

        super().__init__(command_prefix='cuboid', *args, **kwargs)

    async def on_message(self, message):
        args = self.parser.parse_args(message.split())
        print(args)

        await super().on_message(message)


def main():
    with open(CONFIG_PATH) as config_file:
        config = json.load(config_file)

    bot = CuboidBot(config)
    bot.run(config['discord_token'])


if __name__ == '__main__':
    main()
