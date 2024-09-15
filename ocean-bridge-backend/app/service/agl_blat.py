import requests
from fastapi import HTTPException
import json
from app.core.config import settings
from app.models.action_navigation import Action
from app.logging.logging import log_function_call_async

@log_function_call_async
async def perform_data_validation(action_json):
    api_url = settings.AGL_BLAT_TRIAGE_ENDPOINT
    payload = action_json.dict()


    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Request failed with: {response.text}"
            )
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Request error: {str(e)}"
        )
