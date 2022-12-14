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
            cid = ctx.channel.id
            player1id = (await self.bot.db.fetch('SELECT player1id FROM playerlist WHERE matchid = $1', cid))[0]['player1id']
            player2id = (await self.bot.db.fetch('SELECT player2id FROM playerlist WHERE matchid = $1', cid))[0]['player2id']
            player3id = (await self.bot.db.fetch('SELECT player3id FROM playerlist WHERE matchid = $1', cid))[0]['player3id']
            player4id = (await self.bot.db.fetch('SELECT player4id FROM playerlist WHERE matchid = $1', cid))[0]['player4id']
            matchstarted = (await self.bot.db.fetch('SELECT matchstarted FROM match WHERE matchid = $1', cid))[0]['matchstarted']

            #game started/ joined
            if userid in (player1id, player2id, player3id, player4id):
                await ctx.send(f'{username}, you are already in there')
            elif matchstarted == True:
                await ctx.send(f'Too late {username}, game started')

            #find empty seat
            elif player2id == 1:
                await self.bot.db.execute('''
UPDATE playerlist
SET player2id = $1,
WHERE matchid = $2
''', userid, cid)
                await ctx.send(f'{username}joined')
            elif player3id == 1:
                await self.bot.db.execute('''
UPDATE playerlist
SET player3id = $1,
WHERE matchid = $2
''', userid, cid)
                await ctx.send(f'{username}joined')
            elif player4id == 1:
                await self.bot.db.execute('''
UPDATE playerlist
SET player4id = $1,
WHERE matchid = $2
''', userid, cid)
                await ctx.send(f'{username}joined')
            else:
                await ctx.send(f'{username}, the game is full')
            
            
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(join(bot))