from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from typing import List, Union

router = APIRouter(
    prefix="/Health",
    tags=["Health"],
    responses={404: {"description": "Not found"}},
)
@router.get('', 
            )
async def get_health_check():
    return True