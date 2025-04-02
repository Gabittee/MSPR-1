from fastapi import FastAPI
from routers import customers

app = FastAPI()

# Inclusion du routeur des clients
app.include_router(customers.router)
