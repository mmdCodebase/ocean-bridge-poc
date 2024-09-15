import pytest
from fastapi.testclient import TestClient

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from app.main import app
from app.models.autocomplete import AutocompleteResponse

client = TestClient(app)

def test_autocomplete_endpoint():
    workflow_step_id = "62e68aa9-d95a-411a-a4fb-90168b77a438"
    content_id = "BF315462-97A6-42E2-9D05-545F180363F6"
    match = "Hello"
    
    response = client.get(
        "/V1/autocomplete",
        params={
            "workflow_step_id": workflow_step_id,
            "content_id": content_id,
            "match": match
        }
    )
    
    expected_value1 = 'HelloTest1'
    expected_value2 = 'HelloTest2'
    expected_value3 = 'HelloTest3'
    assert response.status_code == 200
    data = response.json()
    data = data['results']
    assert any(item['display_as'] == expected_value1 for item in data)
    assert any(item['display_as'] == expected_value2 for item in data)
    assert any(item['display_as'] == expected_value3 for item in data)

def test_autocomplete_endpoint_compliant():
    response = client.get("/v1/autocomplete")
    assert response.status_code == 200
    assert isinstance(response.json(), AutocompleteResponse)


def test_autocomplete_endpoint_noncompliant():
    response = client.get("/v1/autocomplete")
    assert response.status_code == 422

