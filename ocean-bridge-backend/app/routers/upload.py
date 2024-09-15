from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse
from typing import List, Union
from app.logging.logging import log_function_call
from app.test_data import serve_json
from app.internal.auth import validate_token
from app.service.upload import upload_file_to_s3, is_valid_json

# data
router = APIRouter(
    prefix="/upload",
    tags=["upload"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def upload_test_json(file: UploadFile, isAuthorized = Depends(validate_token)):

    file_content = await file.read()
    if is_valid_json(file_content.decode()):
        try:
            bucket_name = 'oceanbridge-poc-api-backend-json'
            object_name = file.filename
            await file.seek(0)
            upload_file_to_s3(file.file, bucket_name, object_name) 

        except HTTPException as e:
            # logger.exception(e)
            raise e
    
        except Exception as e:
            #logger.exception(e)
            raise HTTPException(status_code=500, detail=str(e))
    
    else:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    
    return True