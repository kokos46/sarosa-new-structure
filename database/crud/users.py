from database import *
from models import User

def get_user(id: int):
    user = db.query(User).get(id)
    return {
        "id": user.id,
        "username": user.username,
        "level": user.level,
        "coins": user.coins,
        "pet_type": user.pet_type
    }

def create_user(username:str, pet_type: str):
    user = User(username=username, pet_type=pet_type)
    db.add(user)
    db.commit()
    return user