from sqlalchemy import Column, Integer, String, JSON
from app.db.postgresql import Base


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    details = Column(JSON)  # Para almacenar la información del Pokémon en formato JSON
