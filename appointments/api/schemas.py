from uuid import UUID

from datetime import datetime

from ninja import Schema

from appointments.application.dtos import AppointmentInDTO, AppointmentOutDTO
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

    def from_domain(self, dto: AppointmentOutDTO):
        return AppointmentIn(
            id=dto.id,
            client=dto.client,
            barber=dto.barber,
            service=dto.service,
            datetime=dto.date_time,
            observation=dto.observation
        )

class AppointmentUpdateDTO(Schema):
    client: UUID | None = None
    barber: UUID | None = None
    service: UUID | None = None
    date_time: datetime | None = None
    status: AppointmentRole | None = None
    observation: str | None = None

    def to_dto(self):
        return AppointmentUpdateDTO(
            client=self.client,
            barber=self.barber,
            service=self.service,
            date_time=self.date_time,
            status=self.status,
            observation=self.observation
        )