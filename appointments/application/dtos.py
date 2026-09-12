from uuid import UUID

from pydantic import BaseModel
from datetime import date,time

from appointments.application.role import AppointmentRole
from appointments.domain.entities import AppointmentEntity

class AppointmentInDTO(BaseModel):
    client: UUID
    barber: UUID
    service: UUID
    date_a: date
    time_a: time
    status: AppointmentRole
    observation: str

class AppointmentOutDTO(BaseModel):
    id: UUID
    client: UUID
    barber: UUID
    service: UUID
    date_a: date
    time_a: time
    status: AppointmentRole
    observation: str

    @classmethod
    def from_domain(cls, entity: AppointmentEntity):
        return cls(
            id = entity.id,
            client = entity.client,
            barber = entity.barber,
            service = entity.service,
            date_a = entity.date_a,
            time_a = entity.time_a,
            status = entity.status,
            observation = entity.observation
        )

class AppointmentUpdateDTO(BaseModel):
    status: AppointmentRole | None = None
    observation: str | None = None
