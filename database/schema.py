from pydantic import BaseModel

class UserBase(BaseModel):
    username: str


class PetBase(BaseModel):
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String(50), index=True)
    # type = Column(String(50), nullable=False)
    # level = Column(Integer, default=1)
    # user_id = Column(Integer, ForeignKey("users.id"))
    #
    # owner = relationship("User", backref="pet")

    name: str
    type: str