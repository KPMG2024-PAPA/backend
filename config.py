from pydantic_settings import BaseSettings
from functools import lru_cache

class mysql_settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    class Config:
        env_file = ".mysql_env"
        extra = "ignore"

class openai_settings(BaseSettings):
    OPENAI_KEY: str

    class Config:
        env_file = ".openai_env"
        extra = "ignore"

@lru_cache()
def get_mysql_setting() -> mysql_settings:
    return mysql_settings()

@lru_cache()
def get_openai_setting() -> openai_settings:
    return openai_settings()
