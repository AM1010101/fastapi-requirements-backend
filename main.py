from fastapi import FastAPI, APIRouter
from app.endpoints import health, item

app = FastAPI()


# add endpoints
app.include_router(health.router, tags=["health"])
app.include_router(item.router, tags=["item"])
