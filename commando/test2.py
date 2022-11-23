from discord.ext import commands
import discord
from db import db


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx, arg):
        await ctx.send('1')
        
        await self.bot.db.fetch('SELECT $1 FROM match WHERE matchid = $2', arg, ctx.channel.id)

        await ctx.send('2')

async def setup(bot):
    await bot.add_cog(test2(bot))