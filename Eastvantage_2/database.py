# SQLite setup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE CONNECTION SETTINGS

SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db"


# `check_same_thread=False` required for SQLite + SQLAlchemy in multithreaded servers

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Create a new session factory
Base = declarative_base() # Base class for all SQLAlchemy models