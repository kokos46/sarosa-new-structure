from . import router
from database import crud, sessionLocal
from database import validator
import database.crud.users as user

@router.get("/items/")
def root():
    user.create_user(sessionLocal, "Gandonio", "lolka")
    return {"status": "success"}

@router.get('/')
def home():
    return "lool"