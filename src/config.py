from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    env_name: str = 'Local'
    port: int = 8000
    app: str = 'src:app'
    host: str = '0.0.0.0'
    base_url: str = 'http://localhost:8000'
    db_url: str = 'sqlite:///./shortener.db'


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
