import json
from typing import Callable, TypeVar

from discord.ext import commands
from exceptions import *

from helpers import db_manager

T = TypeVar("T")


def is_owner() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is an owner of the bot.
    """

    async def predicate(context: commands.Context) -> bool:
        with open("config.json") as file:
            data = json.load(file)
        if context.author.id not in data["owners"]:
            raise UserNotOwner
        return True

    return commands.check(predicate)


def not_blacklisted() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is blacklisted.
    """

    async def predicate(context: commands.Context) -> bool:
        if db_manager.is_blacklisted(context.author.id):
            raise UserBlacklisted
        return True

    return commands.check(predicate)


def is_private_rooms_created() -> Callable[[T], T]:
    """
    This is a custom check for the existed private rooms channel
    """

    def clear_data(data):

        for i, elem in enumerate(data):
            elem = str(elem)
            elem = elem.split(',')[0]
            elem = elem.split('(')[1]
            data[i] = int(elem)
        return data

    async def predicate(context: commands.Context) -> bool:
        voice_channels = context.guild.voice_channels
        created_channels = clear_data(db_manager.get__channels(context.guild.id))
        
        for channel in voice_channels:
            if channel.id in created_channels:
                raise ChannelAlreadyCreated
        if created_channels:
            db_manager.clear__channels(context.guild.id)
            return True
        return True
    return commands.check(predicate)