from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Set up the database connection
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Pbabs@localhost/Diabetes_db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "userss"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Define the request body schema
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Create the FastAPI app
app = FastAPI()

# Define the signup endpoint
@app.post("/signup/")
def signup(user: UserCreate):
    # Create a new user object from the request body
    db_user = User(username=user.username, email=user.email, password=user.password)
    
    # Add the user to the database
    db = SessionLocal()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Return the newly created user
    return {"message": db_user}