from sqlalchemy import Column, Integer, String
from database import Base

class Diabetes(Base):
    __tablename__ = "Users"

    id =  Column(Integer, primary_key=True, nullable=False)
    lastname = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)