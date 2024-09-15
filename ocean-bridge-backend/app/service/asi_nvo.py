import requests
import json
from app.logging.logging import log_function_call 

@log_function_call
def get_navigation_tree(workflow_id):
    api_url = 'https://www.terraportation.com/Dynamic/Login'
    query_params = {
        "parm1": workflow_id
    }

    try: 
        response = requests.get(api_url, params=query_params)
    
        if response.status_code == 200:
            data = {
                "tree": response.json(),
                "headers": response.headers
            }
            return data
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return None

@log_function_call
def get_layout(cookies, workflow_step_id, key_value):
    api_url = 'https://www.terraportation.com/Dynamic/GetWorkflowStep'
    query_params = {
        "workflowStepID": workflow_step_id,
        "keyValue": key_value
    }
    try:
        response = requests.get(api_url, params=query_params, cookies=cookies)
        if response.status_code == 200:
            data = {
               "layout": response.json(),
                "headers": response.headers
            }
            
            return data
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        raise
    except Exception as e:
        print(str(e))
        raise

@log_function_call
def get_datagrid_data(cookies, workflow_step_id, form_id, datagrid_id, key_id, fetch_type):
    api_url = 'https://www.terraportation.com/Dynamic/GetData'
    query_params = {
        "workflowStepID": workflow_step_id,
        "formID" : form_id,
        "dataGridID" : datagrid_id,
        "fetchType" : fetch_type,
        "keyID" : key_id
    }
        
    try: 
        response = requests.get(api_url, params=query_params, cookies=cookies)
        response.raise_for_status()

        if response.status_code == 200:
            data = {
                "datagrid": response.json(),
                "headers": response.headers
            }
            return data
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return None

@log_function_call
def save_workflow_step_data(workflow_step_data):
    api_url = 'https://www.terraportation.com/Dynamic/SaveWorkflowStepData'
    query_params = {
        "workflowStepID": workflow_step_data
    }
    try: 
        response = requests.post(api_url, params=query_params)
    
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return None
@log_function_call
def save_datagrid_data(datagrid_id):
    api_url = 'https://www.terraportation.com/Dynamic/SaveDataGridData'
    query_params = {
        "dataGridID": datagrid_id
    }
    try: 
        response = requests.post(api_url, params=query_params)
    
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return None

@log_function_call   
def save_data(workflow_step_id, form_id, datagrid_id, key_id, fetch_type, data_json):
    api_url = "https://www.terraportation.com/Dynamic/SaveData"

    params = {
        "workflowStepID": workflow_step_id,
        "formID": form_id,
        "dataGridID": datagrid_id,
        "fetchType": fetch_type
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, params=params, headers=headers, json=data_json)
        response.raise_for_status()

        if response.status_code == 200:
            print("Data saved successfully to ASI-NVO")
        else:
            print("Failed to save data to ASI-NVO")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while saving data to ASI-NVO: {str(e)}")

@log_function_call   
def action_navigation(cookies, page_keys, actionable_attributes, row_keys, column_key, data_json):
    api_url = "https://www.terraportation.com/Dynamic/PerformAction20"

    params = {
        "page_keys": json.dumps(page_keys),
        "actionable_attributes": json.dumps(actionable_attributes),
        "row_keys": row_keys,
        "column_key": column_key,
    }
    try:
        response = requests.post(api_url, params=params, json=data_json, cookies=cookies)
        if response.status_code == 200:
            print("Data saved successfully to ASI-NVO")
            return response.json()
        else:
            print("Failed to save data to ASI-NVO")
            #response.raise_for_status()
            print(response.json())
            return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while saving data to ASI-NVO: {str(e)}")
        message = response.json()
        return message

@log_function_call
def get_autocomplete(workflow_step_id, content_id, match):
    api_url = 'https://www.terraportation.com/Dynamic/GetAutoCompleteResults'
    
    params = {
        "workflowStepID": workflow_step_id,
        "content_id": content_id,
        "match": match
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raises an exception for non-2xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request error (e.g., connection error, timeout)
        # You can log the error or perform any other necessary actions
        print(f"Error: {e}")
        print(response.json())
        return e
