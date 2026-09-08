from uuid import UUID

from datetime import datetime

from pydantic import BaseModel

from appointments.domain.entities import AppointmentEntity
from appointments.domain.role import AppointmentRole

class AppointmentInDTO(BaseModel):
    client: UUID
    barber: UUID
    service: UUID
    date_time: datetime
    status: AppointmentRole
    observation: str


class AppointmentOutDTO(BaseModel):
    id: UUID
    client: UUID
    barber: UUID
    service: UUID
    date_time: datetime
    status: AppointmentRole
    observation: str

    @classmethod
    def from_domain(cls, entity: AppointmentEntity):
        return cls(
            id=entity.id,
            client=entity.client.id,
            barber=entity.barber.id,
            service=entity.service.id,
            date_time=entity.date_time,
            status=entity.status,
            observation=entity.observation
        )

class AppointmentUpdateDTO(BaseModel):
    status: AppointmentRole | None = None
    observation: str | None = None
