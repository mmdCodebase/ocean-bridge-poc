from fastapi.testclient import TestClient
import requests
import sys
import json
sys.path.append('../../')
from app.main import app


client = TestClient(app)

def test_get_layout(workflow_id = '9C7F2C1B-308E-49A7-BF6A-0FB8F9E60DE3', workflow_step_id='1aa6a75a-011a-4991-a3b8-fdca96db20a5'):

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
        "workflow_step_id": "5719c1ed-7c65-45d1-820f-c21ee8db2d10",
        "key_value": "15d16c3c-8310-4fef-a9d9-ede4ab2d7eec"
    }

    query_params = {
        "dataGridID" : ['c7548b26-27ac-46dc-8287-a04f37c60d00'],
        }

    response2 = client.get(f"/V1/data/{workflow_step_id}", headers=layout_headers, params=query_params)

    assert response.status_code == 200
    assert response2.status_code == 200