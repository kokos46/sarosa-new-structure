from database import Base, engine
from models import *

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Migration completed")