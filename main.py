import discord
from discord.ext import commands
from discord.utils import get
import platform
import keep_alive

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('c!help'))
filter = []
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    embed = discord.Embed(
        title = 'Those words are not allowed', 
        colour = discord.Colour.red(),
        description = f'{message.author} Dont speak these words in {message.guild}'
    )
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/794760201982312460/795577057123237899/81302-exclamation-line-cartoon-yellow-mark-free-transparent-image-hd.png')
    censor = discord.Embed(
        title = f'Censored Language Detected!!!', 
        colour = discord.Colour.red(), 
        description = f'{message.author} sent something censored in the text'
    )
    censor.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/794760201982312460/795577057123237899/81302-exclamation-line-cartoon-yellow-mark-free-transparent-image-hd.png')

    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/794760201982312460/795577057123237899/81302-exclamation-line-cartoon-yellow-mark-free-transparent-image-hd.png')
    for word in filter:
        if word in message.content:
            await message.delete()
            await message.channel.send(embed = censor)
            await message.author.send(embed = embed)

    if message.content.startswith('c!help'):
        bot_help = discord.Embed(
            title = 'Censor Bot v1.1.0', 
            colour = discord.Colour.orange()

        )
        bot_help.add_field(name = 'About', value=':name_badge: Censor Bot is a moderation bot for bad language. It has an advanced filteration system which can catch vulgar language in texts and delete them.', inline=False)
        bot_help.add_field(name = 'Developer', value=':computer: Kavin Jindal <@!452737276812984330>', inline=False)
        bot_help.add_field(name = 'Prefix', value='`c!`', inline=False)
        bot_help.add_field(name = 'Commands', value='`c!cmd`', inline=False)
        bot_help.add_field(name = 'Bot Version', value='`v1.1.0`', inline=False)
        bot_help.set_thumbnail(url = client.user.avatar_url)
        bot_help.set_author(name = message.author, icon_url= message.author.avatar_url)
        bot_help.set_footer(text = 'Censor Bot v1.1.0 by KJ')

        await message.channel.send(embed = bot_help)

    if message.content.startswith('c!cmd'):
        cmd = discord.Embed(
            title = 'Commands for Censor Bot', 
            colour = discord.Colour.teal()
        )
        cmd.add_field(name = 'Commands', value='`c!stats, c!help, c!credits, c!add, c!info`, c!dev')
        cmd.set_thumbnail(url = client.user.avatar_url)

        await message.channel.send(embed = cmd)

    if message.content.startswith('c!info'):
        info = discord.Embed(
            title = 'Info for Censor Bot', 
            colour=discord.Colour.orange()
        )
        info.add_field(name = 'Info',value=':small_orange_diamond: Developed In   : Python  '
            '\n' 
            '\n' f':small_orange_diamond: Python Version : {platform.python_version()}'
            '\n'
            '\n' f':small_orange_diamond: Discord.py     : {discord.__version__}'
            '\n' 
            '\n'  ':small_orange_diamond: App Version    : v1.1.0'
            '\n' 
            '\n'  ':small_orange_diamond: Hosted on      : Heroku'
            '\n' 
            '\n'  ':small_orange_diamond: Open Source?   : No'
            '\n')
        await message.channel.send(embed = info)
    if message.content.startswith('c!dev'):
        dev = discord.Embed(
            title = 'Censor Bot Developer', 
            colour = discord.Colour.green())
        dev.add_field(name='Developer Info', 
            value=':small_blue_diamond: Developed by     : Kavin Jindal <@!452737276812984330>  '
            '\n' 
            '\n'  ':small_blue_diamond: Github           : https://github.com/kavinjindal'
            '\n' 
            '\n'  ':small_blue_diamond: Email ID         : kavinsjindal@gmail.com'
            '\n' 
            '\n'  ':small_blue_diamond: Discord ID       : KJ#7320'
            '\n' 
            )
        await message.delete()
        await message.channel.send(embed = dev)
    if message.content.startswith('c!add'):
        add = discord.Embed(
            title = 'Add Censor Bot to your server', 
            colour = discord.Colour.orange(), 
            url = 'https://discord.com/api/oauth2/authorize?client_id=795572572363423744&permissions=0&scope=bot'
        )
        await message.channel.send(embed = add)

    if message.content.startswith('c!credits'):
        credits = discord.Embed(
            title = 'Credits for Censor Bot', 
            colour = discord.Colour.orange()
        )
        credits.add_field(name = 'Developer & Owner', value='<@!452737276812984330> Kavin Jindal')
        await message.channel.send(embed = credits)

    if message.content.startswith('c!stats'):
        stats = discord.Embed(title = 'Stats for Censor Bot', 
        colour = discord.Colour.green())
        #await message.channel.send('https://cdn.discordapp.com/emojis/705776148130562120.png?v=1')
        stats.set_author(name='KJ#7320 ', icon_url='https://cdn.discordapp.com/attachments/795927343453306901/795927467516231710/alien-first-contact-cartoon-vector-concept-with-astronaut-futuristic-spacesuit-reaching-hand-e_1441-.jpg')
        stats.add_field(name=f"Stats",
                        value=f":speech_balloon: Servers: {len(client.guilds)}\n:couple: Users: {len(client.users):,}")

        await message.channel.send(embed=stats)
@client.event
async def on_command_error(message):
    if isinstance(error, commands.ClientMissingPermissions):
        await message.channel.send('I am missing the admin permissions, I cant perform the command')

keep_alive.keep_alive()

client.run('')