from pydantic import BaseModel, validator
from typing import Dict, Any, Union
from uuid import UUID
import json

class ValidationMessage(BaseModel):
    table_name: str
    friendly_key_value: str
    column_name: str
    validation_error: str
    data_group_column_id: UUID
    validation_type: int