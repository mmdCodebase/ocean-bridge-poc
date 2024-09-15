from typing import List, Optional
from pydantic import BaseModel, UUID4, UUID5
from .message_model import MessageModel
from .identity_key import IdentityKey


class ValidationModel(BaseModel):
    form_cache_model: Optional[BaseModel]  # Replace with the actual model
    action_id: Optional[str]
    key_field_value: Optional[UUID4]
    data_grid_id: Optional[UUID4]
    workflow_step_id: Optional[UUID4]
    data_location_id: Optional[UUID5]
    previous_workflow_step_id: Optional[UUID4]
    validations: Optional[List[MessageModel]]
    is_detail: Optional[bool]
    action_key_field_values: List[UUID4] = []
    action_key_field_names: List[str] = []
    key_field_values: List[UUID4] = []
    key_field_names: List[str] = []
    inserted_identity_keys: List[IdentityKey] = []

    def add_validation(self, v: MessageModel):
        self.validations.append(v)

    def add_validations(self, v: List[MessageModel]):
        self.validations.extend(v)

    def has_errors(self) -> bool:
        return any(message.is_error for message in self.validations)

    def has_messages(self) -> bool:
        return any(message.is_message for message in self.validations)

    def has_warnings(self) -> bool:
        return any(message.is_warning for message in self.validations)

    def has_new_key(self) -> bool:
        return any(message.is_key for message in self.validations)

    def get_errors(self) -> List[MessageModel]:
        return [message for message in self.validations if message.is_error]

    def get_all_errors_summary(self) -> str:
        return ','.join(error.message for error in self.get_errors())

    def get_warnings(self) -> List[MessageModel]:
        return [message for message in self.validations if message.is_warning]

    def get_messages(self) -> List[MessageModel]:
        return [message for message in self.validations if message.is_message]

    def get_new_keys(self) -> List[MessageModel]:
        return [message for message in self.validations if message.is_key]

    def add_action_key_value(self, k: UUID4, name: str):
        if k not in self.action_key_field_values:
            self.action_key_field_values.append(k)
            self.action_key_field_names.append(name)

    def get_action_key_values(self) -> List[UUID4]:
        return self.action_key_field_values

    def get_action_key_value_string(self) -> str:
        return ','.join(str(g) for g in self.action_key_field_values)

    def add_key_value(self, k: UUID4, key_field_name: str = ""):
        self.key_field_values.append(k)
        self.key_field_names.append(key_field_name)

    def get_key_values(self) -> List[UUID4]:
        return self.key_field_values

    def get_key_values_string(self) -> str:
        return ','.join(str(g) for g in self.key_field_values)

    # You can implement the dump methods based on your debugging needs
    # def dump_keys(self):
    #     ...
