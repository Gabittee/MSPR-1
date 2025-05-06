from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import get_all_items, create_item, update_item, delete_item
from database import get_db
from models import ItemDB
from schemas import *

router = APIRouter()

@router.get("/items/")
def get_items(db: Session = Depends(get_db), response_model=list[Products]):
    return {"items": get_all_items(db)}

@router.post("/items/")
def add_item(item: Products, db: Session = Depends(get_db), response_model=Products):
    new_item = create_item(db, item)
    return {"message": "Item ajouté", "item": new_item}

@router.put("/items/{item_id}")
def modify_item(item_id: int, item: Products, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item)
    if not updated_item:
        return {"error": "Item non trouvé"}
    return {"message": f"Item {item_id} mis à jour", "item": updated_item}

@router.delete("/items/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = delete_item(db, item_id)
    if not deleted_item:
        return {"error": "Item non trouvé"}
    return {"message": f"Item {item_id} supprimé"}