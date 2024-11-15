import discord
from discord.ext import commands


intents = discord.Intents.default()  


intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está online e conectado ao Discord!')

@bot.command()
async def ola(ctx):
    await ctx.send('Olá, mundo!')


bot.run('secret token')
