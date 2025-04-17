from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    level = Column(Integer, default=1)
    coins = Column(Integer, default=0)
    pet_type = Column(String(50), nullable=True)
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "level": self.level,
            "coins": self.coins,
            "pet_type": self.pet_type
        }

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    type = Column(String(50), nullable=False)
    level = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", backref="pet")
