import httpx
from app.core.config import settings
from app.core.exceptions import CustomHTTPException
from app.repositories.pokemon_repository import PokemonRepository


class PokemonService:
    """Service for handling Pokémon data operations."""

    def __init__(self, db):
        self.repository = PokemonRepository(db)

    def get_pokemon(self, identifier: str):
        """Get Pokémon details from the repository or API."""
        db_pokemon = self.repository.get_pokemon_by_name(identifier) or self.repository.get_pokemon_by_id(identifier)
        if db_pokemon:
            return db_pokemon.details

        response = httpx.get(f"{settings.URL_POKEMON}/{identifier}")
        if response.status_code != 200:
            raise CustomHTTPException(detail="Pokemon not found")

        pokemon_data = response.json()
        return self.repository.create_pokemon(pokemon_data)

    def update_pokemon(self, pokemon_id: int, updated_data):
        """Update Pokémon information."""
        return self.repository.update_pokemon(pokemon_id, updated_data)
