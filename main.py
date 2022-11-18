import asyncpg
from discord.ext import commands
import discord.ext.commands
import asyncio
import random
import os
import discord
from os import getenv
from dotenv import load_dotenv


intents = discord.Intents.all()
intents.members = True
prefixxx = ['m.', 'M.']
bot = commands.Bot(command_prefix=prefixxx, case_insensitive=True, activity=discord.Game(name="m.help"), intents=intents)

###########################################################################################################
################################################MAIN_CODE##################################################
###########################################################################################################


@bot.event
async def setup_hook() -> None:
    # this override's Bot.setup_hook and is triggered before the bot starts.

    # creating a database pool
    bot.db_pool: asyncpg.Pool = await asyncpg.create_pool(dburl)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
bot.remove_command('help')

######################################################
#######################COMMANDS#######################
######################################################


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('Command is still on cooldown')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f'**{ctx.author.name}**, this command doesnt exist, check your spellling maybe??')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('an argument is missing')
    else:
        raise error



load_dotenv()
async def main():
    async with bot:
        [await bot.load_extension(f"commando.{file[:-3]}") for file in os.listdir("commando/") if file.endswith(".py")]
        await bot.start(getenv('TOKEN'))

asyncio.run(main())
