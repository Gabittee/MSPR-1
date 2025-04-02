from fastapi import APIRouter
from models.customer import Customer
from controllers.customers_controller import (
    get_all_customers,
    get_customer_by_id,
    create_customer,
    update_customer,
    delete_customer
)

router = APIRouter()

@router.get("/customers")
def get_customers():
    return get_all_customers()

@router.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    return get_customer_by_id(customer_id)

@router.post("/customers")
def add_customer(new_customer: Customer):
    return create_customer(new_customer)

@router.put("/customers/{customer_id}")
def modify_customer(customer_id: str, updated_customer: Customer):
    return update_customer(customer_id, updated_customer)

@router.delete("/customers/{customer_id}")
def remove_customer(customer_id: str):
    return delete_customer(customer_id)
