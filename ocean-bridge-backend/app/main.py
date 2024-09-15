from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import logging
import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))

from routers import workflows, health, navigationtree, upload, layout, data, action, autocomplete, users
from core.config import settings
from models import user
import json
import os

description = '''
# Overall Service flow 
## 0. User logs in and is given a workflow_id
## 1. /V1/workflows/{workflow_id} --> returns Workflow Tree(nav bar)
## User --> clicks on workflow tree and state is set to a "workflowstep_id"
## 2. /V1/workflows/{workflow_id}/workflowstep/{workflowstep_id} --> returns layout of the workflow step

# Possible Path
## 3. /V1/workflows/datagrid/{datagrid_id} --> returns datagrid defintion + data
## 4. /V1/workflows/datagrid/{datagrid_id}/data --> returns datagrid data
## 5. /V1/workflows/actions/{action_id} --> user performs actions


'''

# Create the database tables
# user.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, description=description)

app.include_router(navigationtree.router, prefix="/V1")
app.include_router(health.router)
app.include_router(upload.router, prefix="/V1")
app.include_router(layout.router, prefix="/V1")
app.include_router(data.router, prefix="/V1")
app.include_router(action.router, prefix="/V1")
app.include_router(autocomplete.router, prefix="/V1")
app.include_router(users.router, prefix="/V1")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(dir_path, "config.json")
with open(config_path, "r") as config_file:
    config = json.load(config_file)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Clone the request body for logging
    body_bytes = await request.body()  # Correctly await the coroutine
    body_text = body_bytes.decode('utf-8')  # Assuming the body is UTF-8 encoded text
    logger.info(f'{{"request": "{request.method}", "url": "{request.url}", "body": "{body_text}"}}')

    
    # You must replace the request body for future consumption by the actual endpoint
    async def mock_receive():
        return {"type": "http.request", "body": body_bytes}

    request._receive = mock_receive

    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

async def check_access(request: Request, call_next):
    client_ip = request.client.host
    pre_shared_key = request.headers.get("Pre-Shared-Key")

    if not any(ip["ip"] == client_ip and ip["pre_shared_key"] == pre_shared_key for ip in config["whitelist_ips"]):
        raise HTTPException(status_code=403, detail="Access Denied: IP or pre-shared key not allowed")

    response = await call_next(request)
    return response

@app.get("/")
async def root():
    return {"message": "Hello oceanbridge-poc"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PATCH", "OPTIONS"],  # You can specify the HTTP methods you want to allow
    allow_headers=["*"],  # You can specify the HTTP headers you want to allow,
    expose_headers=["*"]
)

#need access control allow headers / methods





