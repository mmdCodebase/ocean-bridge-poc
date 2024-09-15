from typing import List, Union, Optional
from datetime import date
from pydantic import BaseModel, Json
from uuid import UUID
from .enum import NavigationAction
from enum import Enum as PyEnum
from fastapi import Request

class LayoutRequest(BaseModel):
    workflow_step_id: UUID
    key_value: Union[str, None] = None
    parameter_json: Union[str, None] = None

class DataRequest(BaseModel):
    content_id: UUID 

class DataRequests(BaseModel):
    data_grids: List[DataRequest]

class ActionNavigationRequest(BaseModel):
    page_keys: Json
    actionable_attributes: Json
    row_keys: Optional[str]
    column_key: Optional[str]
    data_json: Json

class FetchType(PyEnum):
    value1 = 'DataGridData'
    value2 = 'PageDataOnly'
    value3 = 'PageDataWithDataGridData'
    value4 = 'FormDataOnly'
    value5 = 'FormDataWithDataGridData'
