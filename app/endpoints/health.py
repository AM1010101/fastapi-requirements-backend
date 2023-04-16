from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Msg(BaseModel):
    msg: str

@router.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@router.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}
