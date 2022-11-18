from discord.ext import commands
import discord


class start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def start(self, ctx):
        try:
            channelid = ctx.channel.id
            await ctx.send('roger that')

            if db[f'{channelid}matchhost'] == ctx.author.id and db[f'{channelid}matchstarted'] == False:
                db[f'{channelid}matchstarted'] = True
                await ctx.send('Match started')
            elif db[f'{channelid}matchhost'] != ctx.author.id:
                await ctx.send('you are not the host')
            elif db[f'{channelid}matchstarted'] == True:
                await ctx.send('Game has already been started')

            await ctx.send('command ended')
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(start(bot))
