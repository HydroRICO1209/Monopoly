from discord.ext import commands
import discord


class stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def stop(self, ctx):
        try:
            userid = ctx.author.id
            username = ctx.author.name
            channelid = ctx.channel.id
            matchhost = (await self.bot.db.fetch('SELECT matchhost FROM match WHERE matchid = $1',(channelid)))[0]["matchhost"]

            if matchhost == userid:
                #all table
                await self.bot.db.execute('''
DELETE FROM match, player, playerlist, property
WHERE matchid = $1
''',channelid)

                await ctx.send(f'Game stopped by {username}')
            else:
                await ctx.send(f'{username}, you are not the host')

        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(stop(bot))