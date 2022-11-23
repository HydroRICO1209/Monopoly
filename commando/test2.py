from discord.ext import commands
import discord


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        await ctx.send('1')
        
        var = await self.bot.db.fetch('SELECT matchstarted FROM match WHERE matchid = $1', (ctx.channel.id))
        await ctx.send(var[0]["matchstarted"])

        await ctx.send('2')

async def setup(bot):
    await bot.add_cog(test2(bot))