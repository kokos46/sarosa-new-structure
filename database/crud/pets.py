from database import *
from models import Pet
from database.schema import PetBase

def get_pet(id: int):
    pet = db.query(Pet).get(id)
    return {
        "id" : pet.id,
        "name": pet.name,
        "type": pet.type,
        "level": pet.level,
        "user_id": pet.user_id
    }


def create_pet(pet: PetBase):
    pet_db = Pet(**pet.model_dump())
    db.add(pet_db)
    db.commit()
    return pet_db