from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import get_all_clients, create_client, update_client, delete_client
from database import get_db
from schemas import ClientCreate

router = APIRouter()

@router.get("/clients/")
def get_clients(db: Session = Depends(get_db)):
    return {"clients": get_all_clients(db)}

@router.post("/clients/")
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = create_client(db, client)
    return {"message": "Client ajouté", "client": new_client}

@router.put("/clients/{client_id}")
def modify_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    updated_client = update_client(db, client_id, client)
    if not updated_client:
        return {"error": "Client non trouvé"}
    return {"message": f"Client {client_id} mis à jour", "client": updated_client}

@router.delete("/clients/{client_id}")
def remove_client(client_id: int, db: Session = Depends(get_db)):
    deleted_client = delete_client(db, client_id)
    if not deleted_client:
        return {"error": "Client non trouvé"}
    return {"message": f"Client {client_id} supprimé"}
