from pydantic import BaseModel
from typing import List, Dict, Optional, Union
from uuid import UUID
from datetime import datetime


class FormFieldAttributes(BaseModel):
    is_column_key_value_required: bool

class ActionFromPageKeys(BaseModel):
    ws_key: Optional[UUID]

class DatagridToolbarAttributes(BaseModel):
    row_sent_type: Optional[str]
    is_row_key_values_required: bool

class DatagridRowAttributes(BaseModel):
    is_row_key_value_required: bool
    is_column_key_value_required: bool

class NavigationAttributes(BaseModel):
    action_nav_ws_id: Optional[UUID]
    action_navigation_type: Optional[str]

class InfoOnlyAttributes(BaseModel):
    action_id: Optional[UUID]
    action_from_ws_id: Optional[UUID]
    action_from_page_keys: Optional[ActionFromPageKeys]
    action_from_form_id: Optional[UUID]
    action_from_data_grid_id: Optional[Union[UUID, str]]
    is_data_sent_for_action: bool

class ActionableAttributes(BaseModel):
    actionable_location: Optional[str]
    action_type: Optional[str]
    special_button_type: Optional[str]
    is_action_refresh_when_complete: Optional[str]
    form_field_attributes: Optional[FormFieldAttributes]
    data_grid_toolbar_attributes: Optional[DatagridToolbarAttributes]
    data_grid_row_attributes: Optional[DatagridRowAttributes]
    navigation_attributes: Optional[NavigationAttributes]
    info_only_attributes: Optional[InfoOnlyAttributes]
