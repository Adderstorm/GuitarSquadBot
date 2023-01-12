import sqlite3 as sql

from database import current_session, private_rooms, blacklist, warns, session


def is_blacklisted(user_id: int) -> bool:
    """
    This function will check if a user is blacklisted.

    :param user_id: The ID of the user that should be checked.
    :return: True if the user is blacklisted, False if not.
    """
    result = current_session.query(blacklist).filter(blacklist.user_id == user_id).first()
    return result.user_id is not None


def add_user_to_blacklist(user_id: int) -> int:
    """
    This function will add a user based on its ID in the blacklist.

    :param user_id: The ID of the user that should be added into the blacklist.
    """
    user = blacklist(user_id=user_id)
    current_session.add(user)
    current_session.commit()
    rows = current_session.query(blacklist).count()
    return rows


def remove_user_from_blacklist(user_id: int) -> int:
    """
    This function will remove a user based on its ID from the blacklist.

    :param user_id: The ID of the user that should be removed from the blacklist.
    """
    user = current_session.query(blacklist).filter(blacklist.user_id == user_id).first()
    current_session.delete(user)
    current_session.commit()
    rows = current_session.query(blacklist).count()
    return rows


def add_warn(user_id: int, server_id: int, moderator_id: int, reason: str) -> int:
    """
    This function will add warn to the database.

    :param user_id: The ID of the user that should be warned.
    :param reason: The reason why the user should be warned.
    """
    user = warns(user_id=user_id, server_id=server_id, moderator_id=moderator_id, reason=reason)
    current_session.add(user)
    current_session.commit()
    rows = current_session.query(warns).filter(warns.user_id == user_id, warns.server_id == server_id).count()
    return rows


def remove_warn(warn_id: int, user_id: int, server_id: int) -> int:
    """
    This function will remove warn from the database.

    :param warn_id: The ID of warn.
    :param user_id: The ID of the user that was warned.
    :param server_id: The ID of the server where the user has been warned
    """
    users = current_session.query(warns).filter(warns.id == warn_id, warns.user_id == user_id, warns.server_id == server_id).all()
    for user in users:        
        current_session.delete(user)
    current_session.commit()
    rows = current_session.query(warns).filter(warns.user_id == user_id, warns.server_id == server_id).count()
    return rows


def get_warnings(user_id: int, server_id: int) -> list:
    """
    This function will get all the warnings of a user.

    :param user_id: The ID of the user that should be checked.
    :param server_id: The ID of the server that should be checked.
    :return: A list of all the warnings of the user.
    """
    result = current_session.query(warns).filter(warns.user_id == user_id, warns.server_id == server_id).all()
    return result

def create__category(guild_id: int, category_id: int, channel_id: int) -> int:
    """
    This function will add a new private channel to the database.

    :param guild_id: The id of the server where category were made
    :param category_id: The id of category bot created at
    :param channel_id: The id of channel bot crated at
    """
    category = private_rooms(server_id=guild_id, category_id=category_id, channel_id=channel_id)
    current_session.add(category)
    current_session.commit()

def get__channel(guild_id: int) -> private_rooms:
    """
    This function will return a list of private channels

    :param guild_id: The id of the server where we are looking for channels
    :return: private_rooms Class
    """
    result = current_session.query(private_rooms).filter(private_rooms.server_id == guild_id).first()
    return result if not type(None) else private_rooms(channel_id=0, server_id=0, category_id=0)

def clear__channels(guild_id: int):
    """
    This function will delete all data about private channels if they were deleted on the discord server

    :param guild_id: The server id that we should clear data for
    """
    channels = current_session.query(private_rooms).filter(private_rooms.server_id == guild_id).all()
    for channel in channels:
        current_session.delete(channel)
    current_session.commit()

def get__voice_channel(catetgory_id: int) -> int:
    """
    
    """
    channel = current_session.query(private_rooms).filter(private_rooms.category_id == catetgory_id).first()