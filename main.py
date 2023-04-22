from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import health, item, cdn

app = FastAPI()


# add endpoints
app.include_router(health.router, tags=["health"])
app.include_router(item.router, tags=["item"])
app.include_router(cdn.router, tags=["cdn"])

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
