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
    
    workflow_step_id_2 = 'c7548b26-27ac-46dc-8287-a04f37c60d00'
    response2 = client.get("/V1/layout/{workflow_step_id_2}", headers=layout_headers)

    print(layout_headers)

    assert response.status_code == 200
    assert response2.status_code == 200