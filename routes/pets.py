from database.schema import PetBase
from . import router
from database.crud import pets


@router.post("/pet/create", response_model=PetBase)
def pet_create(pet: PetBase):
    return pets.create_pet(pet)


@router.get("/pet")
def pet_get(id: int):
    return pets.get_pet(id)