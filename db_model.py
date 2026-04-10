from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from db_conn import engine

base = declarative_base()

class tododb(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    is_done = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))

class UserDB(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

base.metadata.create_all(bind=engine)