from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from typing import List, Union
from app.models.request import ActionNavigationRequest
from app.models.action_navigation import Action
from app.internal.auth import validate_token, parse_cookies
from app.service import asi_nvo, agl_blat
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/action",
    tags=["action"],
    responses={404: {"description": "Not found"}},
)

@router.post('')
async def action_navigation(
                            request: Request,
                            body: ActionNavigationRequest, 
                            isAuthorized = Depends(validate_token)):
    blat_messages = []
    try:
        response_data = ''
        response_data = await agl_blat.perform_data_validation(body)
        blat_messages = response_data['validation_messages']
    except Exception as e:
        print(e)
        print('Failed BLAT process')
        
    auth_token = request.headers.get('Authorization')
    session_id = request.headers.get('SessionID')
    cookies = f"{auth_token};{session_id}"
    cookies = parse_cookies(cookies)

    if response_data == '':
        blat_message = {
            "Message": "BLAT Process Failed",
            "ControlID": "#MvcDynamicField_00000000000000000000000000000000",
            "FieldIdentifier": "00000000-0000-0000-0000-000000000000",
            "MessageWithHTML": "BLAT Process Failed",
            "IsMessage": True,
            "IsWarning": False,
            "IsError": False,
            "IsKey": False,
            "NewKey": "00000000-0000-0000-0000-000000000000",
            "IsSearch": False,
            "ResultsWorkflowStepID": None,
            "SearchClause": None
            }
        blat_messages.append(blat_message)
        response_data = body.data_json
    try:
        result = asi_nvo.action_navigation(cookies, body.page_keys, body.actionable_attributes, body.row_keys, body.column_key, response_data)
        print(result.status_code)
    
    except Exception as e:
        print(e)
        result['messages'].extend(blat_messages)
        return JSONResponse(status_code=500, content=result)
    
    try:
        result['Messages'].extend(blat_messages)
    
    except Exception as e:
        result['messages'].extend(blat_messages)
        return Response(content=json.dumps(result), status_code=500, media_type="application/json")

    return Response(content=json.dumps(result), status_code=200, media_type="application/json")