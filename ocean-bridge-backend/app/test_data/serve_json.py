from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

def get_datagrid_from_file():
    try:
        with open("./app/test_data/DataGrid.json", "r") as file:
            data = json.load(file)
            return JSONResponse(content=data, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"error": "File not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

def get_griddata_from_file():
    try:
        with open("./app/test_data/GridData.json", "r") as file:
            data = json.load(file)
            return JSONResponse(content=data, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"error": "File not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
def get_workflowstep_from_file():
    try:
        with open("./app/test_data/WorkflowStepSimple.json", "r") as file:
            data = json.load(file)
            return JSONResponse(content=data, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"error": "File not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
def get_workflow_from_file():
    try:
        with open("./app/test_data/Workflow.json", "r") as file:
            data = json.load(file)
            return JSONResponse(content=data, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"error": "File not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


def get_workflow_tree_from_file(workflow_id=None):
    if workflow_id == None:
        try:
            with open("./app/test_data/TreeExample.json", "r") as file:
                data = json.load(file)
                return JSONResponse(content=data, status_code=200)
        except FileNotFoundError:
            return JSONResponse(content={"error": "File not found"}, status_code=404)
        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)
        
    else: 
        try:
            with open(f"./app/test_data/{workflow_id}.json", "r") as file:
                data = json.load(file)
                return JSONResponse(content=data, status_code=200)
        except FileNotFoundError:
            return JSONResponse(content={"error": "File not found"}, status_code=404)
        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)