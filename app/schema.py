from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

'''
This file is to define the pydantic schemas to work with the models

User: 
    name: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.now)

UserOut: 
    id: int
    name: str
    email: EmailStr
    created_at: datetime

'''

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.now)
    
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    user_id: str 
    
    