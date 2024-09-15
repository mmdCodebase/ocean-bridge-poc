from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class MessageModel(BaseModel):
    message: Optional[str]
    control_id: Optional[str]
    field_identifier: UUID
    message_with_html: Optional[str]
    is_message: bool
    is_warning: bool
    is_error: bool
    is_key: bool
    new_key: UUID
    is_search: bool
    results_workflow_step_id: Optional[str]
    search_clause: Optional[str]
