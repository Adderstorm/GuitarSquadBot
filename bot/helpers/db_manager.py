import sqlite3 as sql


def is_blacklisted(user_id: int) -> bool:
    """
    This function will check if a user is blacklisted.

    :param user_id: The ID of the user that should be checked.
    :return: True if the user is blacklisted, False if not.
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM blacklist WHERE user_id=?", (user_id,)
        )
    result = cursor.fetchone()
    connection.close()
    return result is not None


def add_user_to_blacklist(user_id: int) -> int:
    """
    This function will add a user based on its ID in the blacklist.

    :param user_id: The ID of the user that should be added into the blacklist.
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO blacklist(user_id) VALUES (?)", (user_id,)
        )
    connection.commit()
    rows = cursor.execute(
        "SELECT COUNT(*) FROM blacklist"
        ).fetchone()[0]
    connection.close()
    return rows


def remove_user_from_blacklist(user_id: int) -> int:
    """
    This function will remove a user based on its ID from the blacklist.

    :param user_id: The ID of the user that should be removed from the blacklist.
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM blacklist WHERE user_id=?", (user_id,)
        )
    connection.commit()
    rows = cursor.execute(
        "SELECT COUNT(*) FROM blacklist"
        ).fetchone()[0]
    connection.close()
    return rows


def add_warn(user_id: int, server_id: int, moderator_id: int, reason: str) -> int:
    """
    This function will add warn to the database.

    :param user_id: The ID of the user that should be warned.
    :param reason: The reason why the user should be warned.
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    # Get the last `id`
    rows = cursor.execute(
        "SELECT id FROM warns WHERE user_id=? AND server_id=? ORDER BY id DESC LIMIT 1", (user_id, server_id,)
        ).fetchone()
    warn_id = rows[0]+1 if rows is not None else 1
    cursor.execute("INSERT INTO warns(id, user_id, server_id, moderator_id, reason) VALUES (?, ?, ?, ?, ?)",
                   (warn_id, user_id, server_id, moderator_id, reason,)
                   )
    connection.commit()
    rows = cursor.execute(
        "SELECT COUNT(*) FROM warns WHERE user_id=? AND server_id=?", (user_id, server_id,)
        ).fetchone()[0]
    connection.close()
    return rows


def remove_warn(warn_id: int, user_id: int, server_id: int) -> int:
    """
    This function will remove warn from the database.

    :param warn_id: The ID of warn.
    :param user_id: The ID of the user that was warned.
    :param server_id: The ID of the server where the user has been warned
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM warns WHERE id=? AND user_id=? AND server_id=?",
                   (warn_id, user_id, server_id,))
    connection.commit()
    rows = cursor.execute(
        "SELECT COUNT(*) FROM warns WHERE user_id=? AND server_id=?", (user_id, server_id,)
        ).fetchone()[0]
    connection.close()
    return rows


def get_warnings(user_id: int, server_id: int) -> list:
    """
    This function will get all the warnings of a user.

    :param user_id: The ID of the user that should be checked.
    :param server_id: The ID of the server that should be checked.
    :return: A list of all the warnings of the user.
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT user_id, server_id, moderator_id, reason, strftime('%s', created_at), id FROM warns WHERE user_id=? AND server_id=?", (user_id, server_id,)
        )
    result = cursor.fetchall()
    connection.close()
    return result

def create__category(guild_id: int, category_id: int, channel_id: int) -> int:
    """
    This function will add a new private channel to the database.

    :param guild_id: The id of the server where category were made
    :param category_id: The id of category bot created at
    :param channel_id: The id of channel bot crated at
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "insert into private_category(server_id, category_id, channel_id) Values(?,?,?)", (guild_id,category_id,channel_id,)
        )
    connection.commit()
    rows = cursor.execute("SELECT COUNT(*) FROM private_category").fetchone()[0]
    connection.close()

def get__channels(guild_id: int) -> list[int]:
    """
    This function will return a list of private channels

    :param guild_id: The id of the server where we are looking for channels
    :return: The list[int] of all created private channels on the server before
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    result = cursor.execute(
        "select channel_id from private_category where server_id=?", (guild_id,)
    ).fetchall()
    cursor.close()
    return result

def clear__channels(guild_id: int):
    """
    This function will delete all data about private channels if they were deleted on the discord server

    :param guild_id: The server id that we should clear data for
    """
    connection = sql.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "delete from private_category where server_id=?", (guild_id,)
    )
    connection.commit()
    cursor.close()