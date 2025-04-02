from sqlalchemy.orm import Session
from models import ItemDB

# Fonction pour récupérer tous les items
def get_all_items(db: Session):
    return db.query(ItemDB).all()

# Fonction pour ajouter un item
def create_item(db: Session, item_data):
    db_item = ItemDB(**item_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Fonction pour mettre à jour un item
def update_item(db: Session, item_id: int, item_data):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        return None
    db_item.name = item_data.name
    db_item.price = item_data.price
    db_item.in_stock = item_data.in_stock
    db.commit()
    db.refresh(db_item)
    return db_item

# Fonction pour supprimer un item
def delete_item(db: Session, item_id: int):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
