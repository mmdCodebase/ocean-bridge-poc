from fastapi.testclient import TestClient
import requests
import random
import sys
import json
sys.path.append('../../')
from app.main import app


client = TestClient(app)

def _find_object_by_content_id(obj, content_id):
    """
    Recursively search for a dictionary with a specific content_id in a nested structure.

    :param obj: The object (dict or list) to search in.
    :param content_id: The content_id value to search for.
    :return: The dictionary that contains the matching content_id, or None if not found.
    """
    if isinstance(obj, dict):
        if obj.get('content_id') == content_id:
            return obj
        for value in obj.values():
            result = _find_object_by_content_id(value, content_id)
            if result is not None:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = _find_object_by_content_id(item, content_id)
            if result is not None:
                return result
    return None

def get_params(actionable_attributes):
    if actionable_attributes['info_only_attributes']['is_data_sent_for_action'] and actionable_attributes is not None:
            if actionable_attributes['actionable_location']:
                print('post all data for page and datagrids')
                
                page_keys = json.dumps(actionable_attributes['info_only_attributes']['action_from_page_keys'])
                actionable_attributes = json.dumps(actionable_attributes)
                row_keys =  ''
                column_key = ''

                params ={
                    "page_keys": page_keys,
                    "actionable_attributes": actionable_attributes,
                    "row_keys": row_keys,
                    "column_key": column_key
                    }
    else:
        params ={
            "page_keys": '',
            "actionable_attributes": '',
            "row_keys": '',
            "column_key": ''
        }

    return params

def _get_page_key(layout):
    return layout["page_keys"]

def _get_data_json_from_layout(layout):
    keys_to_keep = ['fields', 'data_grids']
    data = {k: layout[k] for k in keys_to_keep if k in layout}
    return data

def _alter_data_for_test(data):

    for field in data['fields']:
        if field['content_id'] == 'b24580ce-4ab1-4010-8323-56fe3c6d073a':
            field['m'] = [{"v": str(random.randint(1000,9999)), "d": str(random.randint(1000,9999))}]
            break 
    return data

def test_action_navigation_submit(workflow_id = '9C7F2C1B-308E-49A7-BF6A-0FB8F9E60DE3'):

    headers = {
         "Content-Type": "application/json",
         "Authorization": "12345"
         }

    #GetWorkflow
    response = client.get(f"/V1/navigationtree/{workflow_id}", headers=headers)
    

    #Get WorkflowStep
    layout_request_body = {
        "workflow_step_id": "62e68aa9-d95a-411a-a4fb-90168b77a438",
        "key_value": "CE0D8E31-49E2-438B-8D6C-5AAE62A1B277"
    }
    response2 = client.post("/V1/layout", headers=headers, json=layout_request_body)

    layout = response2.json()
        
    page_key = _get_page_key(layout)
    row_keys = ''
    column_key = ''
    data = _get_data_json_from_layout(layout)
    data = _alter_data_for_test(data)

    result = _find_object_by_content_id(data['fields'], '4fe4fb75-a416-4d7f-85f6-1aa4363cbe1a')
    actionable_attributes = result['actionable_attributes']

    action_navigation_body = {
        "page_keys": json.dumps(page_key),
        "actionable_attributes": json.dumps(actionable_attributes),
        "row_keys": json.dumps(row_keys),
        "column_key": json.dumps(column_key),
        "data_json": json.dumps(data)

    }

    filename = 'action_navigation_body.json'
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dumps(action_navigation_body, f)
    
    response3 = client.post("V1/actionnavigation", headers=headers, json=action_navigation_body)
    
    assert response.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200
    #assert response.json() == True