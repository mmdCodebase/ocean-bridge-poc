from typing import List, Union
from datetime import date
from pydantic import BaseModel
from uuid import UUID
from ..enum import FieldType, DataGridColumnType, DataGridEditableType, DataGridAlign, DataGridSort

class DataGridLayoutColumn(BaseModel):
    title: str
    field: UUID
    initial_order: int
    type: DataGridColumnType
    editable: DataGridEditableType
    render: str
    align: DataGridAlign
    header_align: DataGridAlign
    is_sorting: bool
    default_sort: DataGridSort
    is_filtering: bool
    lookup: str
    custom_sort: str
    custom_filter_and_search: str
    is_hidden: bool
    is_export: bool
    editable_on_row_update: str
    editable_on_row_add: str

class DataGridLayout(BaseModel):
    id: UUID
    columns: List[DataGridLayoutColumn]

class DataGridsLayout(BaseModel):
    datagrids: List[DataGridLayout]