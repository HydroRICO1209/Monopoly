from discord.ext import commands
import discord
from db import db


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        await ctx.send('1')
        
        var = await db(ctx, 'matchplayer')
        await ctx.send(var[0])

        await ctx.send('2')

async def setup(bot):
    await bot.add_cog(test2(bot))