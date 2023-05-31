from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    client_id:str
    client_secret:str
    frontend_url:str
    secret_key:str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

@lru_cache
def get_settings():
    return Settings()

# remember to cd into /backend or else .env won't be read