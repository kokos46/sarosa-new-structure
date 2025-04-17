from sqlalchemy import *
from sqlalchemy.orm import *
import os
from dotenv import load_dotenv

load_dotenv()

user = f"{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}"
host = f"{os.getenv("DB_HOST")}"
db_name = f"{os.getenv("DB_NAME")}"

SQL_COONNECTION = f"mysql+mysqlconnector://{user}@{host}/{db_name}"

engine = create_engine(SQL_COONNECTION)
sessionLocal = Session(engine, future=True)
Base = declarative_base()
