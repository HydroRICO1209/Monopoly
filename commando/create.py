from discord.ext import commands
import discord


class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def create(self, ctx):
        try:
            async with self.bot.db_pool.acquire() as connection:
                matchcreated = await connection.execute(f"SELECT * FROM match WHERE matchid IN {ctx.channel.id}")
            ctx.send('it worked out lmao')
            username = ctx.author.name
            userid = ctx.author.id
            channelid = ctx.channel.id

            if f'{channelid}matchcreated' not in db:
                db[f'{channelid}matchcreated'] = True
                db[f'{channelid}matchplayers'] = [userid]
                db[f'{channelid}matchhost'] = userid
                db[f'{channelid}matchhostname'] = username
                db[f'{channelid}player1money'] = 1500
                db[f'{channelid}matchstarted'] = False
                await ctx.send(f'Successfully created a room by {username}')

                ############################################

                n = 0
                long = ''
                while n < db[f'{channelid}matchplayers']:
                    userid = db[f'{channelid}player{n+1}']
                    long += f'{n+1}) <@{userid}>\n'
                    n += 1

                embed = discord.Embed(
                    description=f'''
Game created by **{db[f'{channelid}matchhostname']}**
{long}
''',
                    color=discord.Color.blue())
                embed.set_author(name='Lobby', icon_url=ctx.author.avatar.url)
                embed.add_field(
                    name='Link', value='[Offcial server](https://discord.gg/ACCYFpPYAj)')
                embed.set_footer(text='Go grab some drinks')
                await ctx.send(embed=embed)

                await ctx.message.delete()
            else:
                await ctx.send('Game has already been created')

        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(create(bot))
