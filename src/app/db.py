import os

import asyncpg


class DB:
    def __init__(self, URL):
        self.conn = None
        self.DATABASE_URL: str = URL

    async def run(self):
        self.conn = await asyncpg.connect(self.DATABASE_URL)
        await self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS heroes (
                id serial primary key,
                name varchar(50) not null,
                description varchar(80) not null
            );
            """
        )


db = DB(os.getenv("DATABASE_URL"))

