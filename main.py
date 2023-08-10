from typing import Union
from fastapi import FastAPI
from models.item_model import Item
from router.router import user


#Creation of an a FastAPI application
app = FastAPI()

app.include_router(user)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"Status": f"El item con el id {item_id} fue actualizado",
            "item_name": item.name,
            "item_id": item_id}