from datetime import date, time
from uuid import UUID

from pydantic import  BaseModel

from costumerservice.domain.entities import CostumerServiceEntity

class CostumerServiceInDTO(BaseModel):
    appointment: UUID
    client: UUID
    barber: UUID
    service: UUID
    date_a: date
    month: int
    deduct: float
    total_value: float
    observation: str

class CostumerServiceOutDTO(BaseModel):
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
    def from_domain(cls, entity: CostumerServiceEntity):
        return CostumerServiceOutDTO(
            id = entity.id,
            appointment = entity.id,
            client = entity.client,
            barber = entity.barber,
            service = entity.service,
            date_a = entity.date_a,
            month = entity.month,
            deduct = entity.deduct,
            total_value = entity.total_value,
            end_value = entity.end_value,
            observation = entity.observation
        )

class ConstumerServiceUpdateDTO(BaseModel):
    deduct: float | None = None
    total_value: float | None = None
    end_value: float | None = None
    observation: str | None = None