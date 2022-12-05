from discord.ext import commands
import discord


class var(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def var(self, ctx, arg):
        await ctx.send(db[f'{ctx.channel.id}{arg}'])

    @commands.command()
    async def delete(self, ctx, arg):
        if ctx.author.id == 757508305256972338:
            if db[f'{ctx.channel.id}{arg}'] == None:
                await ctx.send('Doesnt exist man')
            else:
                del db[f'{ctx.channel.id}{arg}']
                await ctx.send('deleted')

    @commands.command()
    async def deleteall(self, ctx):
        try:
            if ctx.author.id == 757508305256972338:
                keys = db.keys()
                for key in keys:
                    del db[key]
                await ctx.send('deleted all')
        except Exception as e:
            print(e)

    @commands.command()
    async def show(self, ctx):
        try:
            if ctx.author.id == 757508305256972338:
                keys = db.prefix(ctx.channel.id)
                long = 'LIST OF VAR IN THIS SERVER\n'
                if keys == None:
                    await ctx.send('empty database')
                else:
                    for key in keys:
                        value = db[key]
                        long += f'{key}: {value}\n'
                    await ctx.send(long)
        except Exception as e:
            print(e)

    @commands.command()
    async def showall(self, ctx):
        try:
            if ctx.author.id == 757508305256972338:
                keys = db.keys()
                if keys == None:
                    await ctx.send('empty database')
                else:
                    for key in keys:
                        value = db[key]
                        await ctx.send(f'{key}: {value}')
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(var(bot))