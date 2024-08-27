from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

databes_url = os.getenv("DATABASE_URL")

SQLALCHEMY_DATABASE_URL = databes_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False
)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()