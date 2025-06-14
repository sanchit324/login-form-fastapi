from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
from sqlalchemy.ext.declarative import declarative_base

## Wrap in try except block to handle errors
try:
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    print("Error connecting to the database:", e)
    
## Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
