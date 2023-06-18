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
        with open("./bot/helpers/owners.json") as file:
            data = json.load(file)
        if int(context.author.id) not in data['owners']:
            raise UserNotOwner
        return True

    return commands.check(predicate)


def not_blacklisted() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is blacklisted.
    """

    async def predicate(context: commands.Context) -> bool:
        if not db_manager.is_blacklisted(context.author.id):
            raise UserBlacklisted
        return True

    return commands.check(predicate)


def is_private_rooms_created() -> Callable[[T], T]:
    """
    This is a custom check for the existed private rooms channel
    """

    async def predicate(context: commands.Context) -> bool:
        voice_channels = context.guild.voice_channels
        created_channel = db_manager.get__channel(context.guild.id)
        for channel in voice_channels:
            if channel.id == created_channel.channel_id:
                raise ChannelAlreadyCreated
        if created_channel.channel_id != 0:
            db_manager.clear__channels(context.guild.id)
        return True
    return commands.check(predicate)