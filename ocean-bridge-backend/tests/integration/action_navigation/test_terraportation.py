from fastapi.testclient import TestClient
import requests
import random
import sys
import json
sys.path.append('../../')
from app.main import app


client = TestClient(app)

def test_action_navigation_submit(workflow_id ='9C7F2C1B-308E-49A7-BF6A-0FB8F9E60DE3'):
    login_headers = {
         "Content-Type": "application/json",
         "Authorization": "12345"
         }

    #GetWorkflow
    response = client.get(f"/V1/navigationtree/{workflow_id}", headers=login_headers)
    assert response.status_code == 200

    layout_headers = {
        "Content-Type": "application/json",
        "Authorization": response.headers['authorization']

    }

    layout_request_body = {
        "workflow_step_id": "5719c1ed-7c65-45d1-820f-c21ee8db2d10",
        "key_value": "15d16c3c-8310-4fef-a9d9-ede4ab2d7eec"
    }

    response2 = client.post("/V1/layout", headers=layout_headers, json=layout_request_body)
    
    assert response2.status_code == 200

    action_headers = {
        "Content-Type": "application/json",
        "Authorization": response.headers['authorization'],
        "SessionID": response2.headers['sessionid']
    }

    with open('tests/integration/action_navigation/test_payload2.json') as f:
        test_payload = json.load(f)