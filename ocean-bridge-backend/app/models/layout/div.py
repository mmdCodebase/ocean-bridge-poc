from pydantic import BaseModel, constr
from typing import List, Dict, Optional, Union
from uuid import UUID

from ..enum import ContainerType, ContentType, FieldType, DataGridColumnType, DataGridEditableType, DataGridAlign, DataGridSort


class DivStyle(BaseModel):
    container_type: Optional[Union[ContainerType, str]]
    container_text: Optional[str]
    responsiveness: Dict[str, int]
    theme_id: Optional[str]
    class_name: Optional[str]
    class_text: Optional[str]
    colors: Optional[str]
    roundedness: Optional[str]

class DivList(BaseModel):
    order: int
    style: DivStyle
    content: 'DivContent'

class DivContent(BaseModel):
    content_type: Optional[ContentType] = "div_list"
    content_id: Union[UUID, str]
    form_id: Optional[UUID]
    div_list: Optional[List[DivList]]

class DivGrid(BaseModel):
    divgrid: Optional[List[DivList]]
    next_key: Optional[str]

DivList.update_forward_refs()
