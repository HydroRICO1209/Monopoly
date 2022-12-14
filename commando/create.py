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
INSERT INTO match (matchid, matchhostid, matchstarted, matchhostname, matchtotalplayer)
VALUES ($1, $2, False, $3, 1)
''',cid, userid, username)

            #player table
            await self.bot.db.execute('''
INSERT INTO player (matchid, playerid, playermoney, playerbankrupted)
VALUES ($1, $2, 1500, False)
''',cid, userid)

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
            matchtotalplayer = (await self.bot.db.fetch('SELECT matchtotalplayer FROM match WHERE matchid = $1', cid))[0]['matchtotalplayer']
            hostname = (await self.bot.db.fetch('SELECT matchhostname FROM match WHERE matchid = $1', cid))[0]['matchhostname']
            player1id = (await self.bot.db.fetch('SELECT player1id FROM playerlist WHERE matchid = $1', cid))[0]['player1id']
            player2id = (await self.bot.db.fetch('SELECT player2id FROM playerlist WHERE matchid = $1', cid))[0]['player2id']
            player3id = (await self.bot.db.fetch('SELECT player3id FROM playerlist WHERE matchid = $1', cid))[0]['player3id']
            player4id = (await self.bot.db.fetch('SELECT player4id FROM playerlist WHERE matchid = $1', cid))[0]['player4id']
            long = ''

            if matchtotalplayer == 1:
                long += f'1) <@{player1id}>\n'
                if matchtotalplayer == 2:
                    long += f'2) <@{player2id}>\n'
                    if matchtotalplayer == 2:
                        long += f'3) <@{player3id}>\n'
                        if matchtotalplayer == 2:
                            long += f'4) <@{player4id}>\n'

            embed = discord.Embed(
                description=f'''
Game created by **{hostname}**
{long}
''',
                color=discord.Color.blue())
            embed.set_author(name='Lobby', icon_url=ctx.author.avatar.url)
            embed.add_field(
                name='Link', value='[Offcial server](https://discord.gg/ACCYFpPYAj)')
            embed.set_footer(text='Go grab some drinks')
            await ctx.send(embed=embed)

        else:
            await ctx.send(f'**{username}**, Game has already been created')


async def setup(bot):
    await bot.add_cog(create(bot))