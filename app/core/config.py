import os
from dotenv import load_dotenv
from pydantic import BaseModel, PostgresDsn
from typing import ClassVar


load_dotenv()  # Load  variables of .env


class Settings(BaseModel):
    """
    Configurations for the Pokemon Middleware application.

    This class uses Pydantic to define and validate the configurations required for the application.
    The configurations are loaded primarily from environment variables, with default values
    provided for some parameters.

    Attributes:
        ENVIRONMENT (str): Environment in which the application runs (e.g., 'development', 'production').
        PROJECT_NAME (str): Project or application name.
        DATABASE_URL (PostgresDsn): Connection URL to the PostgreSQL database.
        LOG_LEVEL (str): Log level for the application log output.
    """

    # Project
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PROJECT_NAME: str = os.getenv("APP_NAME", "Pokemon Middleware")

    # DataBase
    DATABASE_URL: PostgresDsn = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/pokemon_db")

    # Pokemon URL
    URL_POKEMON: ClassVar[str] = os.getenv("URL_POKEMON", "https://pokeapi.co/api/v2/pokedex")

    # General
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

# Instancia de la configuración
settings = Settings()