from fastapi import FastAPI, HTTPException
from models import User, UserCreate
from database import get_users, create_user, find_user_by_name

app = FastAPI(
    title="Demo API",
    description="Ukázkový projekt pro demonstraci DeepWiki",
    version="1.0.0"
)

@app.get("/")
async def root():
    """
    Uvítací endpoint
    
    Returns:
        dict: Uvítací zpráva
    """
    return {"message": "Vítejte v Demo API"}

@app.get("/users", response_model=list[User])
async def list_users():
    """
    Vrátí seznam všech uživatelů
    
    Returns:
        list[User]: Seznam uživatelů v databázi
    """
    return get_users()

@app.post("/users", response_model=User, status_code=201)
async def add_user(user: UserCreate):
    """
    Vytvoří nového uživatele
    
    Args:
        user: Data nového uživatele
        
    Returns:
        User: Vytvořený uživatel
        
    Raises:
        HTTPException: Pokud uživatel s tímto jménem již existuje
    """
    existing = find_user_by_name(user.name)
    if existing:
        raise HTTPException(status_code=400, detail="Uživatel již existuje")
    return create_user(user)

@app.get("/users/search")
async def search_users(name: str):
    """
    Vyhledá uživatele podle jména
    
    Args:
        name: Jméno k vyhledání
        
    Returns:
        list[User]: Seznam nalezených uživatelů
    """
    users = get_users()
    return [u for u in users if name.lower() in u.name.lower()]