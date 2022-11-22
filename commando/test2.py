from discord.ext import commands
import discord
from db import db


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        try:
            await ctx.send('1')
            
            var = db(ctx, 'matchplayer')
            await ctx.send(var)

            await ctx.send('2')
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(test2(bot))