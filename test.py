from fastapi.testclient import TestClient
from main import app
from database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

Base.metadata.create_all(bind=engine)

client = TestClient(app)

create_payload = {
        "name": "Fabrice",
        "username": "fabrice1618",
        "first_name": "Fabrice",
        "last_name": "Guichard",
        "address_postal_code": "42000",
        "address_city": "Saint-Etienne",
        "profile_first_name": "Fabrice",
        "profile_last_name": "Guichard",
        "company_name": "IRUP"
    }

updated_payload = {
        "name": "Freezer",
        "username": "freeze",
        "first_name": "Freezer",
        "last_name": "Toriyama",
        "address_postal_code": "75001",
        "address_city": "Namek",
        "profile_first_name": "Freez",
        "profile_last_name": "Er",
        "company_name": "Namek Inc"
    }

wrong_payload = {
        "name": 1564653,
        "username": "freeze",
        "first_name": "Freezer",
        "last_name": "Toriyama",
        "address_postal_code": "75001",
        "address_city": "Namek",
        "profile_first_name": "Freez",
        "profile_last_name": "Er",
        "company_name": "Namek Inc"
    }  

def test_get_clients():
    response = client.get("/clients/")
    assert response.status_code == 200
    assert "clients" in response.json()

def test_add_client():

    response = client.post("/clients/", json=create_payload)

    assert response.status_code == 200
    data = response.json()

    print(data)
    assert data["message"] == "Client ajouté"
    assert data["client"]["name"] == create_payload["name"]
    assert data["client"]["username"] == create_payload["username"]
    assert "id" in data["client"]
    assert "created_at" in data["client"]

def test_update_client():

    put_response = client.put(f"/clients/{1}", json=updated_payload)
    assert put_response.status_code == 200

    data = put_response.json()
    print(data)
    assert data["message"] == f"Client {1} mis à jour"
    assert data["client"]["name"] == "Freezer"
    assert data["client"]["address_city"] == "Namek"
    assert data["client"]["username"] == "freeze"

def test_delete_client():

    delete_response = client.delete(f"/clients/{1}")
    assert delete_response.status_code == 200
    delete_data = delete_response.json()
    assert delete_data["message"] == f"Client {1} supprimé"

def test_wrong_type():
    response = client.post("/clients/", json=wrong_payload)
    assert response.status_code == 422 

def test_wrong_type_update():

    response = client.post("/clients/", json=create_payload)
    assert response.status_code == 200

    put_response_wrong = client.put(f"/clients/{1}", json=wrong_payload)
    assert put_response_wrong.status_code == 422