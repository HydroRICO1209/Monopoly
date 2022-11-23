from discord.ext import commands
import discord


class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def create(self, ctx):
        username = ctx.author.name
        userid = ctx.author.id
        cid = ctx.channel.id
        value = await self.bot.db.fetch('SELECT * FROM match WHERE matchid = $1', (ctx.channel.id))
        value = value[0]

        if value == None:
            await self.bot.db.execute('''
INSERT INTO match
matchid = $1,
matchplayer = 1,
matchhost = $2,
matchhostname = $3,
matchstarted = False,
matchproperty = 1
''',(cid, userid, username))
            await ctx.send(f'Successfully created a room by {username}')

            ############################################
            matchplayer = await self.bot.db.fetch('SELECT matchplayer FROM match WHERE matchid = $1', (ctx.channel.id))
            matchplayer = matchplayer[0]

            n = 0
            long = ''
            while n < matchplayer:
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


async def setup(bot):
    await bot.add_cog(create(bot))
