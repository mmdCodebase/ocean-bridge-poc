from fastapi import APIRouter, Depends, HTTPException, Request, Response, Query
from fastapi.responses import FileResponse, JSONResponse
from typing import List, Union, Optional
from pydantic import BaseModel, ValidationError
from app.service import asi_nvo
from uuid import UUID
from app.models.request import DataRequests, FetchType
from app.models.data import Data
from app.internal.auth import validate_token, parse_cookies
from app.service.navigationtree import download_file_from_s3
import json

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)

@router.get('/{workflow_step_id}', #response_model=Data
            )
async def get_datagrid_data(
    request: Request,
    workflow_step_id: UUID,  # Path parameter
    #request: DataRequests,
    response: Response,
    datagrid_ids: List[UUID] = Query(None), 
    form_ids: List[UUID] = Query(None), 
    key_ids: List[UUID] = Query(None),
    fetch_type: FetchType = Query(FetchType.value3),
    isAuthorized = Depends(validate_token)
):
    form_id = ''
    datagrid_id = ''
    key_id = ''
    cookies = request.headers.get('Authorization')
    cookies = parse_cookies(cookies)

    if form_ids:
        form_id = form_ids[0]
    
    if datagrid_ids:
        datagrid_id = datagrid_ids[0]
    
    if key_ids:
        key_id = key_ids[0]
    try:
        data = asi_nvo.get_datagrid_data(cookies=cookies, workflow_step_id=workflow_step_id, form_id=form_id, datagrid_id=datagrid_id, key_id=key_id, fetch_type=fetch_type.value)
        response.headers['SESSIONID'] = data['headers']['Set-Cookie']
        return data['datagrid']

    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content=data)

'''
http://aglsupplychaintest.com:8088/Dynamic/GetDataGridData(string dataGridID) --Returns jsonString either datagriddata or error

 "data_grids": [
    {
      "content_id": "A32CC90C-7949-44CA-85AD-D82070DC8073",
'''

@router.post("/{workflow_step_id}")
async def create_data(
                        request: Data,
                        workflow_step_id: UUID,  # Path parameter
                        datagrid_ids: List[UUID] = Query(None), 
                        form_ids: List[UUID] = Query(None), 
                        key_ids: List[UUID] = Query(None),
                        fetch_type: FetchType = Query(FetchType.value3),
                        isAuthorized = Depends(validate_token)
            ):
    # Invoke the save_data function from app.services.asi_nvo
    workflow_step_id = request.workflow_step_id
    form_id = form_ids[0]
    datagrid_id = datagrid_ids[0]
    key_id = key_ids[0]
    data_json = request

    asi_nvo.save_data(workflow_step_id, form_id, datagrid_id, key_id, fetch_type, data_json)

    return {"message": "Data saved successfully"}
