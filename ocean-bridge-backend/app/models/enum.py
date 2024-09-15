from pydantic import BaseModel
from enum import Enum as PyEnum

class NavigationAction(PyEnum):
    value1 = "pop_up"
    value2 = "navigation"
    value3 = "new_tab"
    value4 = "submit"

class ContainerType(PyEnum):
    field = "field"
    accordion = "accordion"
    panel = "panel"
    tab_group = "tab_group"
    carousel = "carousel"

class ContentType(PyEnum):
    div_list = "div_list"
    data_grid = "data_grid"
    field = "field"
    chart = "chart"

class FieldType(PyEnum):
    text = "text"
    pick_list = "pick_list"
    date_time = "date_time"
    number = "number"
    markdown = "markdown"
    html = "html"
    image = "image"
    empty_space = "empty_space"
    button = "button"
    link = "link"
    hidden = "hidden"

class VariantType(PyEnum):
    outlined = "outlined"
    filled = "filled"
    standard = "standard"
    contained = "contained"
    text = "text"

class DataGridColumnType(PyEnum):
    value1 = 'text'

class DataGridEditableType(PyEnum):
    value1 = "always" # 100% of data validation passed
    value2 = "onUpdate" # Most of data validation is passed
    value3 = "onAdd"
    value4 = "never"

class DataGridAlign(PyEnum):
    value1 = "left"
    value2 = "center"
    value3 = "right"

class DataGridSort(PyEnum):
    value1 = "asc"
    value2 = "desc"    