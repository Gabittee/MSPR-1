from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    postalCode: str
    city: str

class Profile(BaseModel):
    firstName: str
    lastName: str

class Company(BaseModel):
    companyName: str

class Customer(BaseModel):
    name: str
    username: str
    firstName: str
    lastName: str
    address: Address
    profile: Profile
    company: Company
    email: str
    orders: list = []
    createdAt: Optional[str] = None
    id: Optional[str] = None
