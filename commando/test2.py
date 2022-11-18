from discord.ext import commands
import discord


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        async with bot.db_pool.acquire() as connection:
           arg = await connection.execute('SELECT * FROM match')
        await ctx.send(arg)

async def setup(bot):
    await bot.add_cog(test2(bot))
