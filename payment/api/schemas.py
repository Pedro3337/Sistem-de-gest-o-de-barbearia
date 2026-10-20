from datetime import date
from uuid import UUID

from ninja import Schema

from payment.application.dtos import PaymentInDTO, PaymentOutDTO, PaymentUpdateDTO
from payment.domain.roles import PaymentRole, PaymentStatusRole

class PaymentIn(Schema):
    costumer_service: UUID
    payment_method: PaymentRole
    value: float
    date_payment: date
    status: PaymentStatusRole
    month: int
    year: int

    def to_dto(self):
        return PaymentInDTO(
            costumer_service=self.costumer_service,
            payment_method=self.payment_method,
            value=self.value,
            date_payment=self.date_payment,
            status=self.status,
            month=self.month,
            year=self.year
        )

class PaymentOut(Schema):
    id: UUID
    costumer_service: UUID
    payment_method: PaymentRole
    value: float
    date_payment: date
    status: PaymentStatusRole
    month: int
    year: int

    @classmethod
    def from_domain(cls, dto: PaymentOutDTO):
        return cls(
            id=dto.id,
            costumer_service=dto.costumer_service,
            payment_method=dto.payment_method,
            value=dto.value,
            date_payment=dto.date_payment,
            status=dto.status,
            month=dto.month,
            year=dto.year
        )
        

class PaymentUpdate(Schema):
    payment_method: PaymentRole | None = None
    status: PaymentStatusRole | None = None

    def to_dto(self):
        return PaymentUpdateDTO(
            payment_method=self.payment_method,
            status=self.status
        )