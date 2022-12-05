from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

prefixxx = ['m.', 'M.']
bot = commands.Bot(command_prefix=prefixxx, case_insensitive=True, activity=discord.Game(name="rpm start"), intents=intents)


class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, arg):
        try:
            if ctx.author.id == 757508305256972338:
                await self.bot.reload_extension(f'commando.{arg}')
                await ctx.send(f'**{arg}** is reloaded')

        except commands.ExtensionNotLoaded:
            await ctx.send(f'**{arg}** is not loaded')
        except commands.ExtensionNotFound:
            await ctx.send(f'**{arg}** is not found')
        except Exception as e:
            print(e)

    @commands.command()
    async def load(self, ctx, arg):
        try:
            if ctx.author.id == 757508305256972338:
                await self.bot.load_extension(f'commando.{arg}')
                await ctx.send(f'**{arg}** is loaded')

        except commands.ExtensionNotFound:
            await ctx.send(f'**{arg}** is not found')
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f'**{arg}** is already loaded')
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(Reload(bot))