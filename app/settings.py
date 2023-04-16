from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_HOST:str = ""
    POSTGRES_USER:str = ""
    POSTGRES_PASSWORD:str = ""
    POSTGRES_PORT:int = 0
    POSTGRES_DB:str = ""

    class Config:
        env_file = ".env"

