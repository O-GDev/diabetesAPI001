# # from fastapi import FastAPI, Depends
# # from fastapi.params import Body
# # import psycopg2
# # from psycopg2.extras import RealDictCursor
# # import time
# # from sqlalchemy.orm import Session
# # from pydantic import BaseModel
# # import models
# # from database import engine, get_db

# # models.Base.metadata.create_all(bind=engine)

# # app = FastAPI()

# # class newmember(BaseModel):
# #     lastname: str
# #     firstname: str
# #     email: str
# #     password: str

# # class login(BaseModel):
# #     email: str
# #     password: str

# # # while True:
# # #     try:
# # #         conn = psycopg2.connect(host='localhost', database='Diabetes_db' , user='postgres', password='Pbabs',cursor_factory=RealDictCursor)
# # #         cursor = conn.cursor()
# # #         print("Connection Succesful") 
# # #         break
# # #     except Exception as error:
# # #         print("Connection Failed")
# # #         print("Error: ", error)
# # #         time.sleep(2)
        

# # @app.post("/Signup",)
# # def Signup(detailssignup: newmember, db: Session = Depends(get_db)):
# #     # cursor.execute("""INSERT INTO diabetes (last_name, first_name, email, password) VALUES (%s, %s, %s, %s) RETURNING * """,
# #     #                ( detailssignup.lastname, detailssignup.firstname, detailssignup.email, detailssignup.password ))
# #     # new_member1 = cursor.fetchone()
# #     # conn.commit()
# #     new_member = models.Diabetes(lastname=detailssignup.lastname, firstname=detailssignup.firstname, email=detailssignup.email, password=detailssignup.password)
# #     db.add(new_member)
# #     db.commit()
# #     db.refresh(new_member)
# #     return {"message": new_member}

# # @app.get("/sqlalchemy")
# # def Diabetes_table(db: Session = Depends(get_db)):
# #     return{"status": "Successful"}

# # @app.get("/Login",)
# # def Login(detailslogin: login):
# # #   user = cursor.execute("""SELECT (email, password) FROM diabetes """)
    
# #     return {"message": "existing_member"}


# from fastapi import FastAPI ,HTTPException ,File, UploadFile
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from passlib.hash import bcrypt
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List

# # Set up the database connection
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Pbabs@localhost/Diabetes_db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# origins = [
# "http://192.168.43.177:8000"
# ]


# # Define the User model
# class User(Base):
#     __tablename__ = "userss"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)

#     # def set_password(self, password: str):
#     #     salt = scrypt.generate_salt()
#     #     hashed_password = scrypt.hash(password, salt=salt)
#     #     self.password = f"{salt}:{hashed_password}"

#     # def check_password(self, password: str):
#     #     salt, hashed_password = self.password.split(":")
#     #     return scrypt.verify(password, hashed_password, salt=salt)
    
# # Create the tables in the database
# Base.metadata.create_all(bind=engine)

# # Define the request body schema
# class UserCreate(BaseModel):
#     username: str
#     email: str
#     password: str

# class UserLogin(BaseModel):
#     email: str
#     password: str

# # Create the FastAPI app
# app = FastAPI()

# #for signup page
# # Define the signup endpoint
# @app.post("/signup/")
# def signup(user: UserCreate):
#     # Create a new user object from the request body
#     db_user = User(username=user.username, email=user.email, password=user.password)
    
#     # Add the user to the database
#     db = SessionLocal()
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
    
#     # Return the newly created user
#     return {"message": db_user}

# #for login page
# @app.post("/login/")
# def login(user: UserLogin):
#     # Get the user from the database by email
#     db = SessionLocal()
#     db_user = db.query(User).filter(User.email == user.email).first()
    
#     # Check if the user exists and the password is correct
#     if not db_user or db_user.password != user.password:
#         raise HTTPException(status_code=401, detail="Invalid email or password")
    
#     # Return the user
#     return {"message": "successful"}


# class Profile(BaseModel):
#     name: str
#     email: str
#     bio: str


# #for profile page
# @app.post("/profile/")
# async def create_profile(profile: Profile, profile_pic: UploadFile = File(...)):
#     return {"profile": profile, "profile_pic_filename": profile_pic.filename}

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)

# class PasswordResetRequest(BaseModel):
#     email: str

# class UserOut(BaseModel):
#     username: str
#     email: str

# password_reset_requests = []

# @app.post("/forgot-password/")
# async def request_password_reset(request: PasswordResetRequest):
#     # Retrieve user with matching email from database
#     db = SessionLocal()
#     user = db.query(User).filter(User.email == request.email).first()
#     db.close()

#     if user:
#         # Send password reset email to the user's email address
#         return {"message": "Password reset email sent"}
#     else:
#         return {"message": "User not found"}

# @app.get("/users/")
# async def list_users():
#     # Retrieve all users from database
#     db = SessionLocal()
#     users = db.query(User).all()
#     db.close()

#     # Return list of UserOut objects
#     return [UserOut(username=user.username, email=user.email, id=user.id) for user in users]

# @app.delete("/users/{user_email}")
# async def delete_user(user_email: str):
#     # Delete user with given ID from database
#     db = SessionLocal()
#     user = db.query(User).filter(User.email == user_email).first()
#     db.delete(user)
#     db.commit()
#     db.close()

#     return {"message": "User deleted"}



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

from fastapi import FastAPI ,HTTPException ,File, UploadFile,status
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from passlib.hash import bcrypt
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pickle
import json




diabetes_dataset = pd.read_csv('diabetes.csv') 

print(diabetes_dataset.head())
diabetes_dataset.head()

X = diabetes_dataset.drop(columns = 'Outcome', axis=1)

Y = diabetes_dataset['Outcome']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)

X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)


filename = 'diabetes_model.sav'
pickle.dump(classifier, open(filename, 'wb'))


# Set up the database connection
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Gbogo321@localhost/Diabetes_db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

origins = [
"http://192.168.43.177:8000"
]


class model_input(BaseModel):
    
    pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int      

# Define the User model
class User(Base):
    __tablename__ = "userss"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Feed(Base):
    __tablename__ = "feed"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    message1 = Column(String, index=True )
    message2 = Column(String, index=True )
    message3 = Column(String, index=True )

    
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

class Feedbacks(BaseModel):
    email: str
    message1: str
    message2: str
    message3: str



diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# class PredictDiabetes(BaseModel):

# Create the FastAPI app
app = FastAPI()

#for signup page
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


@app.get("/")
async def root():
    raise HTTPException(status_code=404, detail="page not found")
    return {}

#for login page
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


class Profile(BaseModel):
    name: str
    email: str
    bio: str


#for profile page
@app.put("/profile/")
async def create_profile(profile: Profile, profile_pic: UploadFile = File(...)):

    return {"profile": profile, "profile_pic_filename": profile_pic.filename}
@app.get("/profile/")
def get_profiles():
    db = SessionLocal()
    profiles = db.query(User.email,User.username,)
    db.close()
    return{"message": profiles}
class PasswordResetRequest(BaseModel):
    email: str

class UserOut(BaseModel):
    username: str
    email: str


password_reset_requests = []

@app.post("/forgot-password/")
async def request_password_reset(request: PasswordResetRequest):
    # Retrieve user with matching email from database
    db = SessionLocal()
    user = db.query(User).filter(User.email == request.email).first()
    db.close()

    if user:
        # Send password reset email to the user's email address
        return {"message": "Password reset email sent"}
    else:
        return {"message": "User not found"}

@app.get("/users/")
async def list_users():
    # Retrieve all users from database
    db = SessionLocal()
    users = db.query(User).all()
    db.close()

    # Return list of UserOut objects
    return [UserOut(username=user.username, email=user.email, id=user.id) for user in users]

@app.delete("/users/{user_email}")
async def delete_user(user_email: str):
    # Delete user with given ID from database
    db = SessionLocal()
    user = db.query(User).filter(User.email == user_email).first()
    db.delete(user)
    db.commit()
    db.close()

    return {"message": "User deleted"}

@app.post("/feedback/")
def Feedback(feed_back: Feedbacks):
      db = SessionLocal()
      db_feedback = Feed(feed_back.email,feed_back.message1,feed_back.message2,feed_back.message3) 
      db.add(db_feedback)
      db.commit()
      db.refresh(db_feedback)
      return {"message": "Thank you for your feedback!"}

@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if (prediction == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    return{"message" : "successful"} 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
