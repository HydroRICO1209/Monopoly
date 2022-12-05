from discord.ext import commands
import discord


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def help(self, ctx):
        await ctx.send('''
Welcome to this useless bot that does nothing else than Monopoly

__During Game__
m.create - create game (gg)
m.join - join game (gg)
m.leave - leave game (gg)
m.start - start game (gg)
m.stop (gg)

__Misc__
m.rule - rules (gg)
''')


async def setup(bot):
    await bot.add_cog(help(bot))