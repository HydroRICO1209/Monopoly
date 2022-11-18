from discord.ext import commands
import discord
from PIL import Image
from urllib.request import urlopen


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        pass

async def setup(bot):
    await bot.add_cog(test2(bot))
