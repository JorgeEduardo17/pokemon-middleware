from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.postgresql import get_db
from app.services.pokemon_service import PokemonService

router = APIRouter()

@router.get("/")
async def get_pokemon(id: str = None, name: str = None, db: Session = Depends(get_db)):
    """Get Pokémon details by ID or name."""
    service = PokemonService(db)
    if id:
        return service.get_pokemon(id)
    if name:
        return service.get_pokemon(name)
    return {"error": "Provide either id or name."}

@router.put("/{pokemon_id}")
async def update_pokemon(pokemon_id: int, updated_data: dict, db: Session = Depends(get_db)):
    """Update Pokémon details."""
    service = PokemonService(db)
    updated_pokemon = service.update_pokemon(pokemon_id, updated_data)
    if updated_pokemon:
        return updated_pokemon.details
    return {"error": "Pokemon not found."}
