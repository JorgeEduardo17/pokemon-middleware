from fastapi import Request, Response
from sqlalchemy.orm import Session

from app.db.postgresql import get_db
from app.services.pokemon_service import PokemonService


async def pokemon_middleware(request: Request, call_next):
    """Middleware para manejar las consultas a Pokémon."""
    response: Response = await call_next(request)

    # Verificar si se hace una consulta a la ruta de Pokémon
    if request.url.path.startswith("/api/pokemon"):
        db: Session = next(get_db())
        service = PokemonService(db)

        if request.method == "GET":
            identifier = request.query_params.get("id") or request.query_params.get("name")
            if identifier:
                pokemon_data = service.get_pokemon(identifier)
                return Response(content=pokemon_data, media_type="application/json")

    return response
