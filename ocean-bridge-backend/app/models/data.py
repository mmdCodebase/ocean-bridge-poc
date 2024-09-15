from pydantic import BaseModel
from typing import List, Optional, Union, Dict
from uuid import UUID


class FieldOption(BaseModel):
    value: Optional[UUID]
    display_as: Optional[str]
    icon: Optional[str]

class FunctionAttribute(BaseModel):
    icon_group_id: Optional[UUID]
    icon_placement: Optional[str]
    max_pick_allowed: Optional[int]
    options: Optional[List[FieldOption]]
    options_type: Optional[str]
    placeholder: Optional[str]

class DataValue(BaseModel):
    v: Optional[str]
    d: Optional[str]

class Field(BaseModel):
    content_id: Optional[str]
    label: Optional[str]
    is_editable: Optional[bool]
    data_placeholder_value: Optional[str]
    data_original_value: Optional[List[Union[str, int]]]
    data_new_value: Optional[List[Union[str, int]]]
    is_data_required: Optional[bool]
    variant: Optional[str]
    sub_type: Optional[str] = None
    rows: Optional[int] = None
    is_resize_allowed: Optional[bool] = None
    decimal_places: Optional[int] = None
    min: Optional[int] = None
    max: Optional[int] = None
    max_pick_allowed: Optional[int] = None
    options: Optional[List[Dict[str, str]]] = None
    is_disabled: Optional[bool] = None
    functional_attributes: Optional[FunctionAttribute] = None
    m: Optional[List[DataValue]] = None
    o: Optional[List[DataValue]] = None

class DataItem(BaseModel):
    data_item_id: Optional[str]
    o: Optional[List[DataValue]] = None
    m: Optional[List[DataValue]] = None
    tz: Optional[str] = None

class DataRow(BaseModel):
    id: Optional[int]
    data_items : Optional[List[DataItem]]

class DataGrid(BaseModel):
    content_id: Optional[str]
    data: Optional[List[DataRow]]

class Data(BaseModel):
    fields: Optional[List[Field]]
    data_grids: Optional[List[DataGrid]]


