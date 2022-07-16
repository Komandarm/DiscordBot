import random
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='T!')

token = "OTk3ODY5NDM3MDk5MTk2NTE3.GdNNGo.bMHEVlAcWf0H6ePGP2B0XuaYBoqCf_cmIEHnEQ"

curseWord = ['Пидор', 'пидор', 'Блять', 'блять', 'бл', 'бля', 'Чурка', 'чурка', 'нигер', 'Нигер', 'Пидр', 'пидр', 'пидорас', 'Пидорас', 'ЧУРКА', 'ПИДР', 'ПИДОР', 'НИГЕР', 'ПИДОРАС', 'НИГГЕР', 'ниггер', 'Ниггер', 'Хуесос', 'хуесос', 'ХУЕСОС', 'Еблан', 'еблан', 'ЕБЛАН', 'мразь', 'Мразь', 'МРАЗЬ', 'тварь', 'ТВАРЬ', 'Тварь', 'Еблан', 'еблан', 'ЕБЛАН', 'Идиот', 'идиот', 'ИДИОТ']

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention} Было выданно предупреждение пользователю!")
    else:
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```Укажите аргументы```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("```Вы не имеете права```")


@client.event
async def on_ready():
    print("start")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="System TER-190"))

@client.command()
async def helpbot(ctx):
    await ctx.send('Commands: info helpbot projects servers')

@client.command()
async def riu(ctx, *, arg):
    await client.change_presence(activity=discord.Game(name=f"{arg}"))
    embed=discord.Embed(title="Активность бота изменена успешна", color=0x00ff00)
    embed.add_field(name="Активность изменена на", value=f"{arg}", inline=False)
    await ctx.send(embed=embed)
    print(f'[Logs:info] {ctx.author} Изменил активность бота на {arg}')

@client.command()
async def info(ctx):
    await ctx.send("TER-190 This is System Server")

@client.command()
async def projects(ctx):
    await ctx.send("Komandarm made 4 projects: Manager, Manager OS, HelpBOT, TER-190")

@client.command()
async def servers(ctx):
    await ctx.send("SouthWood, Fantasy World")


client.run(token)
