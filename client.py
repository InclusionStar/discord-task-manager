# import discord
from discord.ext import commands
from task_handler import TaskHandler


bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

th = TaskHandler()

sub_commands = {
    'init': th.add(),
    # 'add',
    # 'del',
    # 'clear',
    # 'dl'
}


@bot.event
async def on_ready():
    print(f'Logged as {bot.user}')


@bot.command()
async def help(ctx):
    await ctx.channel.send('```need some help?```')


@bot.command()
async def task(ctx, *args):
    if not args:
        # print('no args')
        return
    sub_commands[args[0]](args[1])
    message = await ctx.channel.fetch_message(799705165401161789)
    await message.edit(content='Smth new :)')
    # await ctx.channel.send(arg)


@bot.command()
async def code(ctx, arg):
    pass


@bot.command()
async def link(ctx, arg):
    pass


with open('token.txt') as f:
    token = f.readline()
    bot.run(token)
