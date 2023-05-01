from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHAMY_DATABASE_URL = os.getenv("DB_URL")
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

db_session = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()
Base.query = db_session.query_property()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()