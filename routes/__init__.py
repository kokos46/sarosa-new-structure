from fastapi import APIRouter

router = APIRouter()

from . import users
from . import pets