from fastapi import APIRouter

from app.api import crud
from app.model.hero import HeroDB, HeroSchema

router = APIRouter(
    prefix="/users"
)


@router.get("/")
async def ping():
    return {"ping": "pong !"}


@router.post("/", response_model=HeroDB, status_code=201)
async def create_hero(data: HeroSchema):
    hero_id = await crud.post(data)
    res_object = {
        id: hero_id,
        "name": data.name,
        "description": data.description
    }
    return res_object
