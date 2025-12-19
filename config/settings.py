from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Define the whitelist of acceptable origins.
    origins: list[str] = [
        "http://localhost:3000"
    ]


# Ensure the settings are only instantiated once.
@lru_cache()
def get_settings() -> Settings:
    return Settings()
