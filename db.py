import asyncio, asyncpg, os

async def db(ctx, arg):
    conn = await asyncpg.connect(os.getenv('DBURL'))

    var = await conn.fetch('SELECT $1 FROM match WHERE matchid = $2',arg ,ctx.channel.id)
    print(var)
    await conn.close()
    return var