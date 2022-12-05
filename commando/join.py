from discord.ext import commands
import discord


class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def join(self, ctx):
        try:
            userid = ctx.author.id
            username = ctx.author.name
            channelid = ctx.channel.id
            playerlist = db[f'{id}matchplayers']

            await ctx.send('roger that')
            if len(playerlist) < 7 and db[f'{channelid}matchstarted'] == False and ctx.author.id not in playerlist:
                db[f'{channelid}matchplayers'].append(userid)

                await ctx.send(f'{username}joined')
            elif len(playerlist) > 8:
                await ctx.send(f'{username}, the game is full')
            elif db[f'{channelid}matchstarted'] == True:
                await ctx.send(f'Too late {username}, game started')
            elif ctx.author.id in playerlist:
                await ctx.send(f'{username}, you are already in there')
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(join(bot))