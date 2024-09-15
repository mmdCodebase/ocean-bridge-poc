from fastapi import APIRouter, Query
from typing import Optional

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
app_dir = current_dir.parent
sys.path.append(str(app_dir))

from service.asi_nvo import get_autocomplete
from models.autocomplete import AutocompleteResponse

router = APIRouter()


@router.get("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(
    workflow_step_id: Optional[str] = Query(None),
    content_id: Optional[str] = Query(None),
    match: Optional[str] = Query(None)
):
    results = get_autocomplete(workflow_step_id, content_id, match)
    return {"results": results}