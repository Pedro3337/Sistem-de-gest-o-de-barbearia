from datetime import date
from typing import List
from uuid import UUID

from costumerservice.infracstuture.models import CostumerService
from payment.domain.entities import PaymentEntity
from payment.domain.repositories import IPaymentRepository
from payment.infracstuture.models import Payment

class PaymentRepository(IPaymentRepository):
    def save(self, entity: PaymentEntity) -> PaymentEntity:
        costumer_service = CostumerService.objects.get(id=entity.costumer_service)
        Payment.objects.update_or_create(
            id=entity.id,
            defaults={
                'costumer_service': costumer_service,
                'payment_method': entity.payment_method,
                'value': entity.value,
                'date_payment': entity.date_payment,
                'status': entity.status,
                'month': entity.month,
                'year': entity.year
            }
        )

        return entity

    def list_payment_all(self) -> List[PaymentEntity]:
        try:
            return [self._to_model(payment) for payment in Payment.objects.all()]
        except Payment.DoesNotExist:
            return None

    def reponse_list_payment_where_date_and_barber_id(self, id: UUID, date: date) -> List[PaymentEntity]:
        ...

    def response_list_payment_where_month(self, month: int) -> List[PaymentEntity]:
        try:
            return [self._to_model(payment) for payment in Payment.objects.filter(month=month)]
        except CostumerService.DoesNotExist:
            return None

    def response_list_payment_where_year(self, year: int) -> List[PaymentEntity]:
        try:
            return [self._to_model(payment) for payment in Payment.objects.filter(year=year)]
        except CostumerService.DoesNotExist:
            return None

    def fin_by_id(self, id: UUID) -> PaymentEntity:
        try:
            return self._to_model(Payment.objects.get(id=id))
        except Payment.DoesNotExist:
            return None

    def _to_model(self, model: Payment) -> PaymentEntity:
        return PaymentEntity(
            id=model.id,
            costumer_service=model.costumer_service.id,
            payment_method=model.payment_method,
            value=model.value,
            date_payment=model.date_payment,
            status=model.status,
            month=model.month,
            year=model.year
        )