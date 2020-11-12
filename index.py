import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print('등장!')

@bot.command()
async def 핑 (ctx):
    await ctx.send('퐁 {0}초'.format(bot.latency))
@bot.command()
async def 니트로프라임(ctx):
    embed = discord.Embed(colour = 808000)
    embed.add_field(name='니트로프라임', value='**```니트로 프라임 3개월 + 섭부2개 [ 8000원 ]```**', inline=Flase)
    await ctx.send(embed=embed)

    bot.run('Nzc2MzEzMjg3NDYwNTE5OTY3.X6zEFg.5IfPG4VNj8QvPCN_f7OjcN-XA0c')