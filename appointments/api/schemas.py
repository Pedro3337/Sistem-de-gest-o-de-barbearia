from uuid import UUID

from ninja import Schema
from datetime import date,time

from appointments.application.dtos import AppointmentInDTO, AppointmentOutDTO
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

    def from_domain(self, dto: AppointmentOutDTO):
        return AppointmentOut(
            id = dto.id,
            client = dto.client,
            barber = dto.barber,
            service = dto.service,
            date_a = dto.date_a,
            time_a = dto.time_a,
            status = dto.status,
            observation = dto.observation
        )

class AppointmentUpdate(Schema):
    status: AppointmentRole | None = None
    observation: str | None = None

    def to_dto(self):
        return AppointmentInDTO(
            status = self.status,
            observation = self.observation
        )