from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from payment.domain.roles import PaymentRole, PaymentStatusRole

@dataclass
class PaymentEntity:
    id: UUID = field(default_factory=uuid4)
    costumer_service: UUID = field(default=None)
    payment_method: PaymentRole = field(default=PaymentRole.pix)
    value: float = field(default=0)
    date_payment: date | None = None
    status: PaymentStatusRole = field(default=PaymentStatusRole.pago)
    month: int = field(default=0)
    year: int = field(default=0)

    def change_payment_method(self, payment_method: PaymentRole):
        self.payment_method = payment_method

    def change_status(self, status: PaymentStatusRole):
        self.status = status