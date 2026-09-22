from datetime import date
from uuid import UUID

from ninja import Schema

from costumerservice.application.dtos import ConstumerServiceUpdateDTO, CostumerServiceInDTO, CostumerServiceOutDTO

class CostumerServiceIn(Schema):
    appointment: UUID
    client: UUID
    barber: UUID
    service: UUID
    date_a: date
    month: int
    deduct: float
    total_value: float
    observation: str

    def to_dto(self) -> CostumerServiceInDTO:
        return CostumerServiceInDTO(
            appointment = self.appointment,
            client = self.client,
            barber = self.barber,
            service = self.service,
            date_a = self.date_a,
            month = self.month,
            deduct = self.deduct,
            total_value = self.total_value,
            observation = self.observation
        )

class CostumerServiceOut(Schema):
    id: UUID
    appointment: UUID
    client: UUID
    barber: UUID
    service: UUID
    date_a: date
    month: int
    deduct: float
    total_value: float
    end_value: float
    observation: str

    @classmethod
    def from_domain(cls, dto: CostumerServiceOutDTO):
        return CostumerServiceOut(
            id = dto.id,
            appointment = dto.id,
            client = dto.client,
            barber = dto.barber,
            service = dto.service,
            date_a = dto.date_a,
            month = dto.month,
            deduct = dto.deduct,
            total_value = dto.total_value,
            end_value = dto.end_value,
            observation = dto.observation
        )

class ConstumerServiceUpdate(Schema):
    deduct: float | None = None
    total_value: float | None = None
    end_value: float | None = None
    observation: str | None = None

    def to_dto(self):
        return ConstumerServiceUpdateDTO (
            deduct=self.deduct,
            total_value=self.total_value,
            end_value=self.end_value,
            observation=self.observation
        )