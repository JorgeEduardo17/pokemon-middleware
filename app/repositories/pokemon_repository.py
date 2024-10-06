from sqlalchemy.orm import Session
from app.models.pokemon import Pokemon

class PokemonRepository:
    """Repository for handling Pokémon data."""

    def __init__(self, db: Session):
        self.db = db

    def get_pokemon_by_name(self, name: str):
        """Retrieve a Pokémon by its name."""
        return self.db.query(Pokemon).filter(Pokemon.name == name).first()

    def get_pokemon_by_id(self, pokemon_id: int):
        """Retrieve a Pokémon by its ID."""
        return self.db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    def create_pokemon(self, pokemon_data):
        """Create a new Pokémon record in the database."""
        new_pokemon = Pokemon(name=pokemon_data["name"], details=pokemon_data)
        self.db.add(new_pokemon)
        self.db.commit()
        self.db.refresh(new_pokemon)
        return new_pokemon

    def update_pokemon(self, pokemon_id: int, updated_data):
        """Update an existing Pokémon record."""
        pokemon = self.get_pokemon_by_id(pokemon_id)
        if pokemon:
            for key, value in updated_data.items():
                setattr(pokemon, key, value)
            self.db.commit()
            self.db.refresh(pokemon)
            return pokemon
        return None
