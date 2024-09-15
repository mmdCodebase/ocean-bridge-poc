from pydantic import BaseModel, Field, UUID4, UUID1, validator, parse_obj_as
from typing import List, Optional, Union, Any, Dict
from datetime import date, datetime
import json

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))

from data import Data
from validation_message import ValidationMessage


class DataGridToolbarAttributes(BaseModel):
    rows_sent_type: Union[str, None]
    is_row_key_values_required: Union[bool, None]
    rows_type: Union[str, None]

class InfoOnlyAttributes(BaseModel):
    action_id: Union[UUID4, None]
    action_from_ws_id: Union[UUID4, None]
    action_from_page_keys: Union[UUID4, None]
    action_from_form_id: Union[UUID4, str, None]
    action_from_data_grid_id: Union[UUID4, None]
    is_data_sent_for_action: Union[bool, None] 

class ActionableAttributes(BaseModel):
    actionable_location: Union[str, None]
    action_type: Union[str, None]
    special_button_type: Union[str, None]
    button_scope: Union[str, None]
    is_action_refresh_when_complete: Union[str, None]
    form_field_attributes: Union[str, None]
    data_grid_toolbar_attributes: Union[DataGridToolbarAttributes, None]
    data_grid_row_attributes: Union[str, None]
    navigation_attributes: Union[str, None]
    info_only_attributes: Union[InfoOnlyAttributes, None]

    @classmethod
    def parse_json(cls, value: Union[str, Dict[str, Any], BaseModel], field_name: str) -> Any:
        if isinstance(value, BaseModel):
            return value  # Return the model instance directly if already deserialized
        elif isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                raise ValueError(f"{field_name} is not valid JSON")
        elif not isinstance(value, dict):
            raise ValueError(f"{field_name} must be a dict, JSON string, or an instance of the expected type")
        return value

    @validator('data_grid_toolbar_attributes', 'info_only_attributes', pre=True)
    def parse_fields(cls, v, field):
        # Directly use the field's name from the 'field' argument correctly
        field_name = field.name  # This is the correct way to access a field's name
        return cls.parse_json(v, field_name)

class PageKey(BaseModel):
    ws_key: Union[UUID4, str, None]

class Action(BaseModel):
    page_keys: PageKey
    actionable_attributes: ActionableAttributes
    data_json: Data
    row_keys: str
    column_key: str

    @classmethod
    def parse_json(cls, value: Union[str, Dict[str, Any], BaseModel], field_name: str) -> Any:
        if isinstance(value, BaseModel):
            return value  # Return the model instance directly if already deserialized
        elif isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                raise ValueError(f"{field_name} is not valid JSON")
        elif not isinstance(value, dict):
            raise ValueError(f"{field_name} must be a dict, JSON string, or an instance of the expected type")
        return value

    @validator('actionable_attributes', 'page_keys', 'data_json', pre=True)
    def parse_fields(cls, v, field):
        # Directly use the field's name from the 'field' argument correctly
        field_name = field.name  # This is the correct way to access a field's name
        return cls.parse_json(v, field_name)
    
class ActionResponse(BaseModel):
    page_keys: PageKey
    actionable_attributes: ActionableAttributes
    data_json: Data
    row_keys: str
    column_key: str
    validation_messages: List[ValidationMessage] = []
    
    @validator('validation_messages', pre=True)
    def validate_validation_messages(cls, v, values, **kwargs):
        if isinstance(v, str):
            # If the input is a string, attempt to parse it as JSON
            try:
                v = json.loads(v)
            except json.JSONDecodeError:
                raise ValueError("validation_messages must be a valid JSON string")
        
        if isinstance(v, list):
            # Ensure each item in the list can be parsed as a ValidationMessage
            result = []

            for item in v:
                if isinstance(item, dict):
                    result.append(ValidationMessage(**item))

                elif isinstance(item, BaseModel):
                    result.append(item)
                else:
                    raise TypeError("Each validation message must be a dict or ValidationMessage instance")
            return result

        raise TypeError("validation_messages must be a list of ValidationMessage instances or a JSON string representing such a list")