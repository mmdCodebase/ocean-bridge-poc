from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

entity_id = str(uuid.uuid4())
token_id = str(uuid.uuid4())


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello oceanbridge-poc"}

def test_get_updated_users():
    start_time = "2024-04-16T00:00:00Z"
    end_time = "2024-04-17T00:00:00Z"

    response = client.get("/V1/authentication/user", params={"updated_start_time": start_time, "updated_end_time": end_time})

    assert response.status_code == 200
    data = response.json()
    assert data["Status"] == "Success"

def test_get_user():
    entity_id = "c24b1518-ccf6-46a7-ae1f-fbd0e7f90f2e"
    response = client.get(f"/V1/authentication/user/{entity_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["Status"] == "Success"

def test_create_authentication_user():
    authentication_user_data = {
        "entity_id": entity_id,
        "contact_id": "2031dcbe-f679-4516-b4b7-4ff30797f814",
        "username": "akamine",
        "user_secret_server_salt": "serversalt",
        "plaintext_password": "plaintextpassword",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "password_updated_on": "2024-03-12T10:00:00Z",
        "ottp_secret_key": "ottp_secret_key",
        "failed_login_attempts_since_last_login": 0,
        "account_status_choice": None,
        "two_factor_authentication_enabled": True,
        "password_recovery_choice": None,
        "second_factor_authentication_choice": None,
        "account_lock_expiry": "2024-04-12T10:00:00Z",
        "last_password_reset": "2024-03-01T10:00:00Z",
        "force_password_change": False,
        "user_is_super_admin" : False,
        "update_at": "2024-03-01T10:00:00Z"
    }

    response = client.post("/V1/authentication/user", json=authentication_user_data)

    assert response.status_code == 201
    assert response.json() == {"Status": "Success", "authentication_user_id": entity_id}


def test_update_authentication_user():
    entity_id = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    update_data = {
        "contact_id": "d7e30acb-766c-457a-a85a-d32aaa6d7d75",
        "username": "john.doe",
        "user_secret_server_salt": "serversalt",
        "plaintext_password": "plaintextpassword",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "password_updated_on": "2024-03-12T10:00:00Z",
        "ottp_secret_key": "ottpsecretkey",
        "failed_login_attempts_since_last_login": 0,
        "account_status_choice": "27725a33-1c22-44a1-81a5-1de5aa42f702",
        "two_factor_authentication_enabled": True,
        "password_recovery_choice": "27725a33-1c22-44a1-81a5-1de5aa42f702",
        "second_factor_authentication_choice": "27725a33-1c22-44a1-81a5-1de5aa42f702",
        "account_lock_expiry": "2024-04-12T10:00:00Z",
        "last_password_reset": "2024-03-01T10:00:00Z",
        "force_password_change": False,
        "user_is_super_admin" : False,
        "updated_at": "2024-04-13T10:00:00Z"
    }

    response = client.patch(f"/V1/authentication/user/{entity_id}", json=update_data)

    assert response.status_code == 202
    assert response.json() == {"Status": "Success", "success": True}


def test_create_authentication_token():
    token_data = {
        "authentication_token_id": token_id,
        "entity_id": "c24b1518-ccf6-46a7-ae1f-fbd0e7f90f2e",
        "ip_address": "127.0.0.1",
        "browser": "Chrome",
        "os": "Windows",
        "device_id": "device1",
        "is_active": True,
        "access_token": "token123",
        "refresh_token": "refresh123",
        "access_token_expired_at": "2024-04-13T10:00:00Z",
        "refresh_token_expired_at": "2024-04-13T10:00:00Z",
        "deleted_at": "2024-04-13T10:00:00Z",
        "updated_at": "2024-04-13T10:00:00Z",
        "last_login_date": "2024-04-13T10:00:00Z"
    }

    response = client.post("/V1/authentication/token", json=token_data)

    assert response.status_code == 201
    assert response.json() == {"Status": "Success", "authentication_token_id": token_id}


def test_update_authentication_token():
    token_id = "3a9b2220-4d5d-4047-9c90-c3fb1253cc14"
    updated_data = {
        "ip_address": "192.30.0.1",
        "browser": "Firefox",
        "os": "Linux",
        "device_id": "device2",
        "is_active": True,
        "access_token": "token456",
        "refresh_token": "refresh456",
        "access_token_expired_at": None,
        "refresh_token_expired_at": None,
        "deleted_at": None,
        "created_at": None,
        "updated_at": None,
        "last_login_date": None
    }

    response = client.patch(f"/V1/authentication/token/{token_id}", json=updated_data)

    assert response.status_code == 202
    assert response.json() == {"Status": "Success", "success": True}



