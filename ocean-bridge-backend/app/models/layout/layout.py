from pydantic import BaseModel
from typing import List, Dict, Optional, Union
from uuid import UUID

from .div import DivGrid, DivList
from .datagrid import DataGridLayout
from .field import Field
from .functional_attributes import NumberAttributes, TextAttributes, ButtonAttributes, ImageAttributes, DateAttributes, PicklistAttributes
from .actionable_attributes import ActionableAttributes


class GridOptions(BaseModel):
    title: str
    pagination: bool
    select_row_column_visible: bool
    edit_row_column_visible: bool
    delete_row_delete_visible: bool
    toolbar_options: List[dict]

class ColumnDefinition(BaseModel):
    content_id: str
    content_name: str
    label: str
    tooltip_description: str
    content_type: str
    variant: str
    data_type: str
    styles: dict
    is_editable: bool
    align: str
    header_align: str
    is_sortable: bool
    is_filterable: bool
    is_hideable: bool
    is_hidden: bool
    is_record_key: bool
    functional_attributes: Optional[Union[NumberAttributes, TextAttributes, ButtonAttributes, ImageAttributes, DateAttributes, PicklistAttributes]]
    actionable_attributes: Optional[ActionableAttributes]

class DataGrid(BaseModel):
    content_id: str
    form_id: Optional[UUID]
    grid_options: GridOptions
    column_definitions: Optional[List[ColumnDefinition]]
    data: Optional[list]

class Layout(BaseModel):
    page_keys: Dict[str, str]
    page_rendering_style: Optional[str]
    div_list: Optional[List[DivList]]
    data_grids: Optional[List[DataGrid]]
    fields: Optional[List[Field]]
