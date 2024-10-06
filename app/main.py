"""
This file is the main entry point for the FastAPI application.
It configures the application, including routes, startup and shutdown events, and logging settings.
"""
from fastapi import FastAPI

from app.api import pokemon
from app.core.config import settings
from app.core.log_config import setup_logging
from app.db.postgresql import init_db

app = FastAPI(title=settings.PROJECT_NAME)  # Create a FastAPI instance for the application.


# Incluir los routers de los endpoints
app.include_router(pokemon.router, prefix="/api/pokemon", tags=["pokemon"])


setup_logging()  # Setup of logging module

@app.on_event("startup")
def startup_db_client():
    init_db()

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to the Pokémon API!"}

