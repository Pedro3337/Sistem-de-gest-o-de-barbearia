from abc import ABC, abstractmethod
from datetime import date
from typing import List
from uuid import UUID

from payment.domain.entities import PaymentEntity
from payment.infracstuture.models import Payment

class IPaymentRepository(ABC):
    @abstractmethod
    def save(self, entity: PaymentEntity) -> PaymentEntity:
        ...

    @abstractmethod
    def list_payment_all(self) -> List[PaymentEntity]:
        ...

    @abstractmethod
    def reponse_list_payment_where_date_and_barber_id(self, id: UUID, date: date) -> List[PaymentEntity]:
        ...

    @abstractmethod
    def response_list_payment_where_month(self, month: int) -> List[PaymentEntity]:
        ...

    @abstractmethod
    def response_list_payment_where_year(self, year: int) -> List[PaymentEntity]:
        ...

    @abstractmethod
    def fin_by_id(self, id: UUID) -> PaymentEntity:
        ...

    @abstractmethod
    def _to_model(self, model: Payment) -> PaymentEntity:
        ...