from fastapi import FastAPI, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class newmember(BaseModel):
    lastname: str
    firstname: str
    email: str
    password: str

class login(BaseModel):
    email: str
    password: str

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='Diabetes_db' , user='postgres', password='Pbabs',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connection Succesful") 
#         break
#     except Exception as error:
#         print("Connection Failed")
#         print("Error: ", error)
#         time.sleep(2)
        

@app.post("/Signup",)
def Signup(detailssignup: newmember, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO diabetes (last_name, first_name, email, password) VALUES (%s, %s, %s, %s) RETURNING * """,
    #                ( detailssignup.lastname, detailssignup.firstname, detailssignup.email, detailssignup.password ))
    # new_member1 = cursor.fetchone()
    # conn.commit()
    new_member = models.Diabetes(lastname=detailssignup.lastname, firstname=detailssignup.firstname, email=detailssignup.email, password=detailssignup.password)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return {"message": new_member}

@app.get("/sqlalchemy")
def Diabetes_table(db: Session = Depends(get_db)):
    return{"status": "Successful"}

@app.get("/Login",)
def Login(detailslogin: login):
#   user = cursor.execute("""SELECT (email, password) FROM diabetes """)
    
    return {"message": "existing_member"}