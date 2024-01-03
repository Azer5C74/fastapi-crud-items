from fastapi import FastAPI, HTTPException

app = FastAPI()

items = [
    {"id": 1, "name": "Cheese", "price": 4.5}
]

@app.post("/items/")
def create_item(item: dict):
    items.append(item)
    return {"message": "Item created successfully", "item": item}

@app.get("/items/")
def read_items():
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    print ('item_id', item_id)
    if item_id < len(items):
        return {"item": items[item_id]}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    if item_id < len(items):
        items[item_id] = updated_item
        return {"message": "Item updated successfully", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        deleted_item = items.pop(item_id)
        return {"message": "Item deleted successfully", "deleted_item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
