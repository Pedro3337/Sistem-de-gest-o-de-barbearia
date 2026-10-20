from datetime import date
from uuid import UUID

from pydantic import BaseModel

from payment.domain.entities import PaymentEntity
from payment.domain.roles import PaymentRole, PaymentStatusRole

class PaymentInDTO(BaseModel):
    costumer_service: UUID
    payment_method: PaymentRole
    value: float
    date_payment: date
    status: PaymentStatusRole
    month: int
    year: int

class PaymentOutDTO(BaseModel):
    id: UUID
    costumer_service: UUID
    payment_method: PaymentRole
    value: float
    date_payment: date
    status: PaymentStatusRole
    month: int
    year: int

    @classmethod
    def from_domain(cls, entity: PaymentEntity):
        return cls(
            id=entity.id,
            costumer_service=entity.costumer_service,
            payment_method=entity.payment_method,
            value=entity.value,
            date_payment=entity.date_payment,
            status=entity.status,
            month=entity.month,
            year=entity.year
        )
        

class PaymentUpdateDTO(BaseModel):
    payment_method: PaymentRole | None = None
    status: PaymentStatusRole | None = None