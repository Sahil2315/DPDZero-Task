from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

dbURL = os.getenv("DB_URL")

engine = create_engine(dbURL)

def getSession():
    with Session(engine) as session:
        yield session