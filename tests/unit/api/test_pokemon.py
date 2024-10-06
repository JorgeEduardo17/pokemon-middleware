from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_pokemons():
    """Test the endpoint for retrieving a list of Pokémon."""
    response = client.get("/api/pokemon/")
    assert response.status_code == 200
    assert "results" in response.json()

def test_get_pokemon():
    """Test the endpoint for retrieving a specific Pokémon by ID."""
    response = client.get("/api/pokemon/1")
    assert response.status_code == 200
    assert response.json()["name"] == "bulbasaur"
