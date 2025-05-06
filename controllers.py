from sqlalchemy.orm import Session
from models import ItemDB
from schemas import *

# Fonction pour récupérer tous les items
def get_all_items(db: Session):
    test =  db.query(ItemDB).all
    return [itemdb_to_products(test) for test in test]

# Fonction pour ajouter un item
def create_item(db: Session, item_data: Products):
    db_item = ItemDB(
        name=item_data.name,
        price=item_data.details.price,
        description=item_data.details.description,
        color=item_data.details.color,
        stock=item_data.stock,
        id=item_data.id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return itemdb_to_products(db_item)

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

def itemdb_to_products(item: ItemDB) -> Products:
    return Products(
        name=item.name,
        details=Details(
            price=item.price,
            description=item.description,
            color=item.color
        ),
        stock=item.stock,
        id=item.id
    )