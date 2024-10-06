from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core.config import settings

# Create an SQLAlchemy engine instance. `pool_pre_ping` enables pre-pinging the database to ensure connections are alive
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Create a scoped session factory bound to the scope of the web request for thread safety.
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base class for declarative class definitions. Used to declare models.
Base = declarative_base()


def init_db():
    """
    Initializes the database by creating all tables based on the models inherited from `Base`.
    This function should be called at application startup to ensure the database schema is up to date.
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Generator function that yields a new SQLAlchemy session for each request and ensures it is
    closed when the request ends. This function is intended to be used as a dependency in FastAPI
    endpoint functions to provide a session for database operations.

    Yields:
        Session: A new SQLAlchemy session for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()