# main.py
from fastapi import FastAPI
from api import crud

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: dict):
    return crud.create_item(item)

@app.get("/items/")
def read_items():
    return crud.read_items()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return crud.read_item(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    return crud.update_item(item_id, updated_item)

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return crud.delete_item(item_id)
