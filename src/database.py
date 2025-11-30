from models import User, UserCreate
from typing import List

# In-memory databáze pro demo
users_db: List[User] = [
    User(id=1, name="Jan Novák", email="jan@example.com"),
    User(id=2, name="Eva Svobodová", email="eva@example.com"),
]

def get_users() -> List[User]:
    """Vrátí všechny uživatele"""
    return users_db

def create_user(user: UserCreate) -> User:
    """Vytvoří nového uživatele"""
    new_id = max([u.id for u in users_db], default=0) + 1
    new_user = User(id=new_id, **user.dict())
    users_db.append(new_user)
    return new_user

def find_user_by_name(name: str) -> User | None:
    """Najde uživatele podle jména"""
    for user in users_db:
        if user.name.lower() == name.lower():
            return user
    return None