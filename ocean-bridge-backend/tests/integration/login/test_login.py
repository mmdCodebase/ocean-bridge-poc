import logging
from fastapi.testclient import TestClient
import requests
import random
import sys
import json
sys.path.append('../../')
from app.main import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TestClient(app)

def test_login(workflow_id = '9C7F2C1B-308E-49A7-BF6A-0FB8F9E60DE3'):

    headers = {
         "Content-Type": "application/json",
         "Authorization": "12345"
         }

    #GetWorkflow
    response = client.get(f"/V1/navigationtree/{workflow_id}", headers=headers)
    logger.info(response.json())
    assert response.status_code == 200