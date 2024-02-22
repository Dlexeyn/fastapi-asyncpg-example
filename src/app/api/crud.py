from app.db import db
from app.model.hero import HeroSchema


async def post(data: HeroSchema):
    result = await db.conn.fetchrow(
        """
        INSERT into public.heroes values (default, $1, $2) returning id;
        """,
        data.name,
        data.description
    )
    return result
