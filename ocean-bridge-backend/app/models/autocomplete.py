from pydantic import BaseModel
from typing import Optional

class AutocompleteItem(BaseModel):
    value: str
    display_as: str
    icon: Optional[str]

class AutocompleteResponse(BaseModel):
    results: list[AutocompleteItem]