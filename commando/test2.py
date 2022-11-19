from discord.ext import commands
import discord


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        try:
            await ctx.send('1')
            async with bot.db_pool.acquire() as connection:
                # creating a connection cursor if needed
                async with connection.cursor() as cursor:
                    await cursor.fetch("SELECT part_id, part_name FROM parts ORDER BY part_name")
            await ctx.send('2')
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(test2(bot))