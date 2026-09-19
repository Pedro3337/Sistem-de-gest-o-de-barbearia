from uuid import UUID

from barber.infrasctuture.models import Barber
from clients.infrasctuture.models import Client
from pydantic import BaseModel
from datetime import date,time

from appointments.application.role import AppointmentRole
from appointments.application.domain.entities import AppointmentEntity
from service.infrasctuture.models import Service

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
    name_client: str
    name_barber: str
    name_service: str
    value_service: float

    @classmethod
    def from_domain(cls, entity: AppointmentEntity):
        client = Client.objects.get(id=entity.client)
        barber = Barber.objects.get(id=entity.barber)
        service = Service.objects.get(id=entity.service)
        return cls(
            id = entity.id,
            client = entity.client,
            barber = entity.barber,
            service = entity.service,
            date_a = entity.date_a,
            time_a = entity.time_a,
            status = entity.status,
            observation = entity.observation,
            name_client = client.user.name,
            name_barber = barber.user.name,
            name_service = service.name,
            value_service = service.value
        )

class AppointmentUpdateDTO(BaseModel):
    status: AppointmentRole | None = None
    observation: str | None = None
