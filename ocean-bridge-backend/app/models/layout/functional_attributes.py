from pydantic import BaseModel
from typing import List, Optional, Union
from uuid import UUID
from datetime import datetime


class NumberAttributes(BaseModel):
    decimal_places: Optional[int]
    min: Optional[int]
    max: Optional[int]
    default_value: Optional[int]
    decimal_separator: Optional[int]
    is_percent: Optional[bool]
    prefix: Optional[str] = "$"
    suffix: Optional[str] = ""
    float_allowed: Optional[bool] = False
    display_as: Optional[str] = "default"
    icon_group_id: Optional[UUID] = ""
    display_type: Optional[str] = ""
    # icon_fill

class TextAttributes(BaseModel):
    sub_type: Optional[Union[str("email"), str("password")]]
    rows: Optional[int]
    is_resize_allowed: Optional[bool] = False

class ButtonAttributes(BaseModel):
    # Revist during the action navigation JSON discussion
    pass

class ImageAttributes(BaseModel):
    # To be decided
    pass

class DateAttributes(BaseModel):
    sub_type: Optional[Union[str("date"), str("time"), str("date_time")]]
    date_time_format: Optional[datetime]
    is_show_timezone: Optional[bool] = False

class Options(BaseModel):
    value: Optional[str]
    display_as: Optional[str]
    icon: Optional[str]

class PicklistAttributes(BaseModel):
    options_type: Optional[Union[str("local"), str("api")]]
    display_type: Optional[Union[
        str("radio_button"),
        str("check_box"),
        str("drop_down"),
        str("sttate_button"),
        str("toggle_switch")
    ]] = "radio_button" # It should be updated
    max_pic_allowed: Optional[int] = 1
    options: Optional[List[Options]]
    icon_group_id: Optional[str]
    icon_placement: Optional[Union[str("before"), str("after"), str("icon_only"), str("text_only")]]
    placeholder: Optional[str]
