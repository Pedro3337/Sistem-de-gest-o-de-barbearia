from datetime import datetime
from uuid import UUID

from ninja import Schema

from clients.application.dtos import ClientInDTO

class ClientIn(Schema):
    user_id: UUID

    def to_dto(self):
        return ClientInDTO(
            user_id=self.user_id
        )

class ClientOut(Schema):
    id: UUID
    user_id: UUID
    date_register: datetime

    def from_domain(self, dto):
        return ClientOut(
            id=dto.id,
            user_id=dto.user_id,
            date_register=dto.date_register
        )

