from . import router
import database.crud.users as users


@router.get('/user')
def get_user(id: int):
    user = users.get_user(1)
    return user


@router.post('/user/create')
def create_user(username: str, pet_type: str):
    user = users.create_user(username, pet_type)
    return {"message": "success"}