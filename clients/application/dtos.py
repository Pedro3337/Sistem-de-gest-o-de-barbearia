from datetime import datetime
from uuid import UUID

from ninja import Schema

class ClientInDTO(Schema):
    user_id: UUID

class ClientOutDTO(Schema):
    id: UUID
    user_id: UUID
    date_register: datetime

    def from_domain(cls, entity):
        return cls(
            id=entity.id,
            user_id=entity.user_id,
            date_register=entity.date_register
        )

