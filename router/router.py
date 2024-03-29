from fastapi import APIRouter, HTTPException
from schema.user_schema import UserSchema
from config.db import  conn
from models.users import users

#Dividir las rutas de la aplicación
user = APIRouter()

@user.get("/")
def root():
    return {"Message": "Hi, I am FastAPI with a router"}

@user.post("/users")
def create_user(data_user: UserSchema):
    new_user = data_user.dict()
    conn.execute(users.insert().values(new_user))
    return {"message": f"El usuario {data_user.username} ha sido creado"}

@user.get("/users")
def get_user(Id = int):
    user =  conn.execute(f"SELECT * FROM users WHERE id = {Id}").fetchone()
    
    if user is None:
        raise HTTPException(status_code=404, detail= f"El usuario no con el ID {Id} no ha sido registrado")
    
    return user
    
