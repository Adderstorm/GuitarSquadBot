from discord.ext import commands


class UserBlacklisted(commands.CheckFailure):
    """
    Thrown when a user is attempting something, but is blacklisted.
    """

    def __init__(self, message="User is blacklisted!"):
        self.message = message
        super().__init__(self.message)


class UserNotOwner(commands.CheckFailure):
    """
    Thrown when a user is attempting something, but is not an owner of the bot.
    """

    def __init__(self, message="User is not an owner of the bot!"):
        self.message = message
        super().__init__(self.message)

class ChannelAlreadyCreated(commands.CheckFailure):
    """
    Thtow when a user is trying to create second private channel(or category)
    """
    
    def __init__(self, message='Private channels category already exist'):
        self.message = message
        super().__init__(self.message)
