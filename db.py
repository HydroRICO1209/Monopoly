import asyncio
import asyncpg

async def db(ctx, arg):
    conn = await asyncpg.connect(os.getenv('DBURL'))

    var = await conn.fetch('SELECT $1 FROM match WHERE matchid = $2',arg ,ctx.channel.id)
    return var
    await conn.close()

asyncio.get_event_loop().run_until_complete(main())