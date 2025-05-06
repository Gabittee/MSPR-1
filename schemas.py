from pydantic import BaseModel
from datetime import datetime

class ClientBase(BaseModel):
    name: str
    username: str
    first_name: str
    last_name: str
    address_postal_code: str
    address_city: str
    profile_first_name: str
    profile_last_name: str
    company_name: str

class ClientCreate(ClientBase):
    pass  # Pour les données à créer

class Client(ClientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True