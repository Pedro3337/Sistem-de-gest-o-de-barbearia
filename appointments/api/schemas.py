from uuid import UUID

from ninja import Schema
from datetime import date,time

from appointments.application.dtos import AppointmentInDTO, AppointmentOutDTO, AppointmentUpdateDTO
from appointments.application.role import AppointmentRole

class AppointmentIn(Schema):
    client: UUID
    barber: UUID
    service: UUID
    date_a: date
    time_a: time
    status: AppointmentRole
    observation: str

    def to_dto(self):
        return AppointmentInDTO(
            client = self.client,
            barber = self.barber,
            service = self.service,
            date_a = self.date_a,
            time_a = self.time_a,
            status = self.status,
            observation = self.observation
        )

class AppointmentOut(Schema):
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
    def from_domain(cls, dto: AppointmentOutDTO):
        return cls(
            id = dto.id,
            client = dto.client,
            barber = dto.barber,
            service = dto.service,
            date_a = dto.date_a,
            time_a = dto.time_a,
            status = dto.status,
            observation = dto.observation,
            name_client = dto.name_client,
            name_barber = dto.name_barber,
            name_service = dto.name_service,
            value_service = dto.value_service
        )

class AppointmentUpdate(Schema):
    status: AppointmentRole | None = None
    observation: str | None = None

    def to_dto(self):
        return AppointmentUpdateDTO(
            status = self.status,
            observation = self.observation
        )