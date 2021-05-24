#!/usr/bin/env python

import json
import argparse
from pathlib import Path

import discord.ext.commands


__version__ = '0.1.0'


CONFIG_PATH = Path('config.json')


class CuboidBot(discord.ext.commands.Bot):
    def __init__(self, config: dict, *args, **kwargs):
        self.name = 'cuboid'
        self.config = config

        parser = argparse.ArgumentParser(
            prog=self.name,
            description='Bot manager for Discord',
            exit_on_error=False
        )
        parser.add_argument('--version', action='store_true')
        subparsers = parser.add_subparsers(dest='subcommand')
        parser_version = subparsers.add_parser(
            'version',
            help="show program's version number and exit"
        )
        self.parser = parser

        super().__init__(command_prefix=self.name, *args, **kwargs)

    async def on_ready(self):
        print(f'{self.name} started.')

    async def on_message(self, message: discord.Message):
        if message.content.startswith(f'{self.name} '):
            argv = message.content.split()[1:]
            try:
                args = self.parser.parse_args(argv)
            except argparse.ArgumentError:
                pass
            else:
                print(args)
                if args.version or args.subcommand == 'version':
                    await message.channel.send(__version__)

        await super().on_message(message)


def main():
    with open(CONFIG_PATH) as config_file:
        config = json.load(config_file)

    bot = CuboidBot(config)
    print('starting..')
    bot.run(config['discord_token'])


if __name__ == '__main__':
    main()
