from fastapi import APIRouter

#Dividir las rutas de la aplicación

user = APIRouter()

@user.get("/")
def root():
    return {"Message": "Hi, I am FastAPI with a router"}