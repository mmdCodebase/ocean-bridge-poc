from typing import List, Union
from datetime import date
from pydantic import BaseModel
from uuid import UUID
from enum import Enum as PyEnum

class TreeTypes(PyEnum):
    value1= "group"
    value2= "link"
    
class WorflowTree(BaseModel):
    order: Union[str, None] = None
    type: Union[TreeTypes, None] = None
    text: Union[str, None] = None
    icon: Union[str, None] = None
    icon_group_id: Union[str, None] = None
    workflow_step_id: Union[UUID,str, None] = None
    is_expanded: Union[bool, None] = None
    is_selected: Union[bool, None] = None
    is_collapsible: Union[bool, None] = None
    is_has_divider: Union[bool, None] = None
    tree: Union[List['WorflowTree'], None] = None

class WorkflowTrees(BaseModel):
    tree : List['WorflowTree']

