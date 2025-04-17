from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    level = Column(Integer, default=1)
    coins = Column(Integer, default=0)
    pet_type = Column(String(50), nullable=True)  # тип питомца

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # имя питомца
    type = Column(String(50), nullable=False)  # тип питомца
    level = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", backref="pet")
