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
            async with connection.cursor() as cursor:
                await cursor.fetch("SELECT part_id, part_name FROM parts ORDER BY part_name")
                rows = cur.fetchall()
            await ctx.send('2')
            await ctx.send(rows)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(test2(bot))


