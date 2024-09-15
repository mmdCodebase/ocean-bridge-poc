from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from typing import List, Union
from uuid import UUID
import json

from app.models.request import LayoutRequest
from app.internal.auth import validate_token, parse_cookies
from app.models.layout.layout import Layout
from app.service.navigationtree import download_file_from_s3
from app.service import asi_nvo

router = APIRouter(
    prefix="/layout",
    tags=["layout"],
    responses={404: {"description": "Not found"}},
)

@router.post('')
async def post_layout(
    request: Request, 
    layout_request: LayoutRequest,
    response: Response,
    isAuthorized = Depends(validate_token)
):
    try:
        workflow_step_id = layout_request.workflow_step_id
        key_value = layout_request.key_value
        cookies = request.headers.get('Authorization')
        cookies = parse_cookies(cookies)
        data = asi_nvo.get_layout(cookies=cookies, workflow_step_id=workflow_step_id, key_value=key_value)
        response.headers['SESSIONID'] = data['headers']['Set-Cookie']
        return data['layout']
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content='data')

@router.get('/{workflow_step_id}')
async def get_layout(
    request: Request,
    workflow_step_id: str,
    response: Response,
    isAuthorized = Depends(validate_token)
):
    try:
        cookies = request.headers.get('Authorization')
        cookies = parse_cookies(cookies)
        data = asi_nvo.get_layout(cookies=cookies, workflow_step_id=workflow_step_id, key_value="")
        response.headers['SESSIONID'] = data['headers']['Set-Cookie']
        return data['layout']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
