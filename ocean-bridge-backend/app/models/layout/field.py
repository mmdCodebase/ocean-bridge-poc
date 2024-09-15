from pydantic import BaseModel
from typing import List, Union, Optional
from uuid import UUID

from ..data import DataValue
from ..enum import FieldType, VariantType, DataGridColumnType, DataGridEditableType, DataGridAlign, DataGridSort
from .functional_attributes import NumberAttributes, TextAttributes, ButtonAttributes, ImageAttributes, DateAttributes, PicklistAttributes
from .actionable_attributes import ActionableAttributes

class Field(BaseModel):
    content_id : UUID
    content_name: Optional[str]
    label: Optional[str]
    form_id: Optional[UUID]
    tooltip_description: Optional[str]
    data_type: Optional[FieldType]
    variant: Optional[VariantType]
    is_editable: Optional[bool] = True
    is_disabled: Optional[bool] = False
    is_data_required: Optional[bool] = False
    is_record_key: Optional[bool] = False
    o: Optional[List[DataValue]]
    m: Optional[List[DataValue]]
    functional_attributes: Optional[Union[NumberAttributes, TextAttributes, ButtonAttributes, ImageAttributes, DateAttributes, PicklistAttributes]]
    actionable_attributes: Optional[ActionableAttributes]
