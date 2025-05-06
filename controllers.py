from models import Itemdb
from schemas import ClientCreate
from sqlalchemy.orm import Session

# Lister tous les clients
def get_all_clients(db: Session):
    return db.query(Itemdb).all()

# Ajouter un client
def create_client(db: Session, client_data: ClientCreate):
    db_client = Itemdb(**client_data.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Mettre à jour un client
def update_client(db: Session, client_id: int, client_data: ClientCreate):
    db_client = db.query(Itemdb).filter(Itemdb.id == client_id).first()
    if not db_client:
        return None
    for field, value in client_data.dict().items():
        setattr(db_client, field, value)
    db.commit()
    db.refresh(db_client)
    return db_client

# Supprimer un client
def delete_client(db: Session, client_id: int):
    db_client = db.query(Itemdb).filter(Itemdb.id == client_id).first()
    if not db_client:
        return None
    db.delete(db_client)
    db.commit()
    return db_client
