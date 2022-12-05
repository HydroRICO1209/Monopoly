from discord.ext import commands
import discord


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test(self, ctx):
        try:
            id = ctx.channel.id
            hostid = db[f'{id}matchhost']

            embed = discord.Embed(
                description='Board',
                color=discord.Color.blue())
            embed.set_image(
                url='https://static.wikia.nocookie.net/monopoly/images/a/a5/Monopoly_Board_Game_%28UK%29.jpg/revision/latest/scale-to-width-down/1000?cb=20220120173735')
            embed.set_author(name=f'<@{hostid}>'),
            embed.set_footer(text='Go grab some drinks')
            await ctx.send(embed=embed)

            await ctx.message.delete()
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(test(bot))