from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    """Základní model uživatele"""
    name: str
    email: EmailStr

class UserCreate(UserBase):
    """Model pro vytvoření uživatele"""
    pass

class User(UserBase):
    """Model uživatele s ID"""
    id: int
    
    class Config:
        from_attributes = True