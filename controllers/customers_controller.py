import json
import os
from models.customer import Customer

API_FILE = "./data/customers.json"

def get_all_customers():
    try:
        with open(API_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def get_customer_by_id(customer_id: str):
    customers = get_all_customers()
    for customer in customers:
        if customer["id"] == customer_id:
            return customer
    return {"error": "Customer not found"}

def create_customer(new_customer: Customer):
    customers = get_all_customers()
    new_id = str(max([int(c["id"]) for c in customers] + [0]) + 1)
    new_customer_data = new_customer.dict()
    new_customer_data["id"] = new_id
    customers.append(new_customer_data)

    with open(API_FILE, "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4)

    return {"message": "Customer created successfully", "customer": new_customer_data}

def update_customer(customer_id: str, updated_customer: Customer):
    customers = get_all_customers()

    for customer in customers:
        if customer["id"] == customer_id:
            customer.update(updated_customer.dict())
            with open(API_FILE, "w", encoding="utf-8") as file:
                json.dump(customers, file, indent=4)
            return {"message": "Customer updated successfully", "customer": customer}
    
    return {"error": "Customer not found"}

def delete_customer(customer_id: str):
    customers = get_all_customers()

    customers = [c for c in customers if c["id"] != customer_id]

    with open(API_FILE, "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4)

    return {"message": "Customer deleted successfully"}
