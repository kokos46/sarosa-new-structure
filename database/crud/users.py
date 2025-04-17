from database import *
from models import User

def create_user(db:Session, username:str, pet_type: str):
    user = User(username=username, pet_type=pet_type)
    db.add(user)
    db.commit()

