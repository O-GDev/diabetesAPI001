# from fastapi import FastAPI, Depends
# from fastapi.params import Body
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# import models
# from database import engine, get_db

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# class newmember(BaseModel):
#     lastname: str
#     firstname: str
#     email: str
#     password: str

# class login(BaseModel):
#     email: str
#     password: str

# # while True:
# #     try:
# #         conn = psycopg2.connect(host='localhost', database='Diabetes_db' , user='postgres', password='Pbabs',cursor_factory=RealDictCursor)
# #         cursor = conn.cursor()
# #         print("Connection Succesful") 
# #         break
# #     except Exception as error:
# #         print("Connection Failed")
# #         print("Error: ", error)
# #         time.sleep(2)
        

# @app.post("/Signup",)
# def Signup(detailssignup: newmember, db: Session = Depends(get_db)):
#     # cursor.execute("""INSERT INTO diabetes (last_name, first_name, email, password) VALUES (%s, %s, %s, %s) RETURNING * """,
#     #                ( detailssignup.lastname, detailssignup.firstname, detailssignup.email, detailssignup.password ))
#     # new_member1 = cursor.fetchone()
#     # conn.commit()
#     new_member = models.Diabetes(lastname=detailssignup.lastname, firstname=detailssignup.firstname, email=detailssignup.email, password=detailssignup.password)
#     db.add(new_member)
#     db.commit()
#     db.refresh(new_member)
#     return {"message": new_member}

# @app.get("/sqlalchemy")
# def Diabetes_table(db: Session = Depends(get_db)):
#     return{"status": "Successful"}

# @app.get("/Login",)
# def Login(detailslogin: login):
# #   user = cursor.execute("""SELECT (email, password) FROM diabetes """)
    
#     return {"message": "existing_member"}


from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import bcrypt
from fastapi.middleware.cors import CORSMiddleware

# Set up the database connection
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Pbabs@localhost/Diabetes_db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

origins = [
"http://192.168.43.177:8000"
]


# Define the User model
class User(Base):
    __tablename__ = "userss"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # def set_password(self, password: str):
    #     salt = scrypt.generate_salt()
    #     hashed_password = scrypt.hash(password, salt=salt)
    #     self.password = f"{salt}:{hashed_password}"

    # def check_password(self, password: str):
    #     salt, hashed_password = self.password.split(":")
    #     return scrypt.verify(password, hashed_password, salt=salt)
    
# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Define the request body schema
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
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

@app.post("/login/")
def login(user: UserLogin):
    # Get the user from the database by email
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    
    # Check if the user exists and the password is correct
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Return the user
    return {"message": "successful"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)