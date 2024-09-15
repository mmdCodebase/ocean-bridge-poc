from pydantic import BaseModel, UUID4, validator
from typing import Optional
import uuid

class IdentityKey(BaseModel):
    field_data_group_id: Optional[str]
    field_value: str
    field_name: Optional[str]
    field_table: Optional[str]

    @validator('field_value', pre=True)
    def validate_field_value(cls, v):
        if isinstance(v, uuid.UUID):
            return str(v)
        return v

    @validator('field_data_group_id', 'field_name', 'field_table', pre=True, always=True)
    def convert_uuid_to_string(cls, v):
        if isinstance(v, uuid.UUID):
            return str(v)
        return v

    @classmethod
    def from_guid_and_table(cls, value: UUID4, name: str, table: str):
        return cls(field_value=value, field_name=name, field_table=table)

    @classmethod
    def from_guid_and_dgc(cls, value: UUID4, dgc: UUID4):
        return cls(field_value=value, field_data_group_id=dgc)

    def is_table_column_equal(self, table_name: str, column_name: str) -> bool:
        # Perform case-insensitive comparison
        return (self.field_name.lower() == column_name.lower()) and (self.field_table.lower() == table_name.lower())

# Example usage
# identity_key = IdentityKey.from_guid_and_table(uuid.uuid4(), 'name', 'table')
# print(identity_key.is_table_column_equal('table', 'name'))
