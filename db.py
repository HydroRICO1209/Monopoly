async def db(arg):
    conn = await asyncpg.connect(os.getenv('DBURL'))
