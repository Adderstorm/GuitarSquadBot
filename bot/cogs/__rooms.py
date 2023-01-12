import discord
from discord.ext import commands
from discord.ext.commands import Context
from helpers import checks
from helpers.db_manager import create__category

class Rooms(commands.Cog, name='__rooms'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @checks.not_blacklisted()
    async def on_voice_state_update(context: Context, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        #entry_room = get__channel(context.guild.id)
        entry_room = 1058488459146317875
        print(before, after, member, sep='\n')
        if(before.channel != entry_room and after.channel == entry_room):
            pass

    @commands.hybrid_group(
        name='voice',
        desription='Help you manage private channel'
    )
    @checks.not_blacklisted()
    async def voice(self, context: Context):
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                title="Voice",
                description="You need to specify a subcommand.\n\n**Subcommands:**\n`kick` - Kick a user from your channel.\n`limit` - Sets a limit for channel.\n`owner` - Set a new onwer for this channel\n`mute` - Mute a spicific user in channel\n`_invite` - Warning! Only owner option",
                color=0xE02B2B
            )
            await context.send(embed=embed)
    
    @voice.command(
        base='voice',
        name='_invite',
        desription='Create entry point for the private rooms'
    )
    @checks.is_owner()
    @checks.is_private_rooms_created()
    async def create__channel(self, context: Context, category_name: str = 'Приватные каналы'):
        channel_name='➕・Создать'

        category = await context.guild.create_category(name=category_name)
        channel = await context.guild.create_voice_channel(name=channel_name, category=category)

        create__category(context.guild.id, category.id, channel.id)

        embed = discord.Embed(
            title="Voice channel created",
            description="Succesful :)",
            color=0x32CD32
        ).add_field(
            name="P.S.",
            value="You can also rename category or channel"
        )
        await context.send(embed=embed)

    @commands.command(
        base='voice',
        name='rename',
        description='Rename your own channel name'
    )
    @checks.not_blacklisted()
    async def rename(self, context: Context, *, message: str):
        pass

    @commands.command(
        base='voice',
        name='hide',
        description='Hide or show your own room'
    )
    @checks.not_blacklisted()
    async def hide(self, context: Context):
        pass

    @voice.command(
        base='voice',
        name='kick',
        description='Kick abussive member'
    )
    @checks.not_blacklisted()
    async def kick(self, context: Context, user: discord.User):
        pass

    @voice.command(
        base='voice',
        name='limit',
        desription='Set the limit for the voice channel'
    )
    @checks.not_blacklisted()
    async def limit(self, context: Context, numb: int):
        pass

    @voice.command(
        base='voice',
        name='owner',
        description='Set new channel owner'
    )
    @checks.not_blacklisted()
    async def owner(self, context: Context, newuser: discord.User):
        pass
    

async def setup(bot):
    await bot.add_cog(Rooms(bot))