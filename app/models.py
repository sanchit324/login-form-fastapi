import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    
    def __repr__(self) -> str:
        return f"User(name={self.name}, email={self.email}, password={self.password}, created_at={self.created_at})"
    