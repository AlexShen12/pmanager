# external

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.globals.config import settings

#If want type validation, most likely have to instantiate within app and call back to here using a funciton that may raise issues.

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
  # Define in .env file
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

