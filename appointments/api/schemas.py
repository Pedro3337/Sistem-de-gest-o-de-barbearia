from uuid import UUID

from datetime import datetime

from ninja import Schema

from appointments.application.dtos import AppointmentInDTO, AppointmentOutDTO, AppointmentUpdateDTO
from appointments.domain.entities import AppointmentEntity
from appointments.domain.role import AppointmentRole

class AppointmentIn(Schema):
    client: UUID
    barber: UUID
    service: UUID
    date_time: datetime
    status: AppointmentRole
    observation: str

    def to_dto(self) -> AppointmentInDTO:
        return AppointmentInDTO(
            client=self.client,
            barber=self.barber,
            service=self.service,
            date_time=self.date_time,
            status=self.status,
            observation=self.observation
        )

class AppointmentOut(Schema):
    id: UUID
    client: UUID
    barber: UUID
    service: UUID
    date_time: datetime
    status: AppointmentRole
    observation: str

    @classmethod
    def from_domain(cls, dto: AppointmentOutDTO):
        return AppointmentOutDTO(
            id=dto.id,
            client=dto.client,
            barber=dto.barber,
            service=dto.service,
            date_time=dto.date_time,
            status=dto.status,
            observation=dto.observation
        )

class AppointmentUpdate(Schema):
    status: AppointmentRole | None = None
    observation: str | None = None

    def to_dto(self):
        return AppointmentUpdateDTO(
            status=self.status,
            observation=self.observation
        )