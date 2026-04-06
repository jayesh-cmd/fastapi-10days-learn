from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from db_conn import engine

base = declarative_base()

class tododb(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    is_done = Column(Boolean, default=False)

base.metadata.create_all(bind=engine)