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

            if db[f'{channelid}matchhost'] == userid:
                tobedeleted = db.prefix(channelid)
                for stuff in tobedeleted:
                    del db[stuff]
                await ctx.send(f'Game stopped by {username}')
            else:
                await ctx.send(f'{username}, you are not the host')

        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(stop(bot))
