from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import FileResponse
from typing import List, Union

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))
from app.logging.logging import log_function_call
from app.test_data import serve_json
from app.models.tree import WorkflowTrees
from app.internal.auth import validate_token
from app.service.navigationtree import download_file_from_s3
import json
from uuid import UUID

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))
from app.service.asi_nvo import get_navigation_tree

# data
router = APIRouter(
    prefix="/navigationtree",
    tags=["navigationtree"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{workflow_id}", response_model=WorkflowTrees)
async def get_navigationtree(
    workflow_id: UUID,
    response: Response,
    isAuthorized: bool = Depends(validate_token)
):
    try:
        data = get_navigation_tree(workflow_id)
        #response.headers['Set-Cookie'] = data['headers']['Set-Cookie']
        response.headers['Authorization'] = data['headers']['Set-Cookie']
        
        return data['tree']
    except Exception as e:
        print(e)
        try:
            bucket_name = 'oceanbridge-poc-api-backend-json'
            file_name = f"{workflow_id}.json"
            file_content = download_file_from_s3(bucket_name, file_name)
            json_data = json.loads(file_content)
            return json_data
    
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="File content is not valid JSON")
        
        except HTTPException as e:
            # logger.exception(e)
            raise e
    
        except Exception as e:
            #logger.exception(e)
            raise HTTPException(status_code=500, detail=str(e))
