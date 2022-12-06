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
        created = await self.bot.db.fetch('SELECT * FROM match WHERE matchid = $1', (ctx.channel.id))

        if created == []:
            #match table
            await self.bot.db.execute('''
INSERT INTO match (matchid, matchhost, matchstarted, matchhostname, matchtotalplayer)
VALUES ($1, $2, False, $3, 1)
''',cid, userid, username)

            #player table
            await self.bot.db.execute('''
INSERT INTO player (playerid, playermoney, playerbankrupted)
VALUES ($1, 1500, False)
''',userid)

            #playerlist table
            await self.bot.db.execute('''
INSERT INTO playerlist (matchid, player1id, player2id, player3id, player4id)
VALUES ($1, $2, 1, 1, 1)
''',cid, userid)

            #property table
            await self.bot.db.execute('''
INSERT INTO property (matchid, pro1, pro2, pro3)
VALUES ($1, 0, 0, 0)
''',cid)

            await ctx.send(f'Successfully created a room by **{username}**')

            ############################################
            matchplayer = await (self.bot.db.fetch('SELECT matchplayer FROM match WHERE matchid = $1', (ctx.channel.id)))[0]['matchplayer']
            hostname = await (self.bot.db.fetch('SELECT matchhostname FROM match WHERE matchid = $1', (ctx.channel.id)))[0]['matchhostname']
            
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
            await ctx.send(f'**{username}**, Game has already been created')


async def setup(bot):
    await bot.add_cog(create(bot))