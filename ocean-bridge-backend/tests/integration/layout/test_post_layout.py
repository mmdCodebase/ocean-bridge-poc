from fastapi.testclient import TestClient
import requests
import sys
import json
sys.path.append('../../')
from app.main import app


client = TestClient(app)

def test_get_layout(workflow_id = '9C7F2C1B-308E-49A7-BF6A-0FB8F9E60DE3'):

    login_headers = {
         "Content-Type": "application/json",
         "Authorization": "12345"
         }

    #GetWorkflow
    response = client.get(f"/V1/navigationtree/{workflow_id}", headers=login_headers)

    layout_headers = {
        "Content-Type": "application/json",
        "Authorization": response.headers['authorization']

    }

    layout_request_body = {
        "workflow_step_id": "62e68aa9-d95a-411a-a4fb-90168b77a438",
        "key_value": "CE0D8E31-49E2-438B-8D6C-5AAE62A1B277"
    }

    response2 = client.post("/V1/layout", headers=layout_headers, json=layout_request_body)

    assert response.status_code == 200
    assert response2.status_code == 200
