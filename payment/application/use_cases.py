from typing import List
from uuid import UUID

from payment.application.dtos import PaymentInDTO, PaymentOutDTO, PaymentUpdateDTO
from payment.domain.entities import PaymentEntity
from payment.domain.repositories import IPaymentRepository

class RegisterPaymentUseCase:
    def __init__(self, payment_repo: IPaymentRepository):
        self.payment_repo = payment_repo

    def execute(self, dto: PaymentInDTO) -> PaymentOutDTO:
        payment_entity = PaymentEntity(
            costumer_service=dto.costumer_service,
            payment_method=dto.payment_method,
            value=dto.value,
            date_payment=dto.date_payment,
            status=dto.status,
            month=dto.month,
            year=dto.year
        )

        return PaymentOutDTO.from_domain(
            self.payment_repo.save(payment_entity)
        )

class ResponseListAllPaymentUseCase:
    def __init__(self, payment_repo: IPaymentRepository):
        self.payment_repo = payment_repo

    def execute(self) -> List[PaymentOutDTO]:
        payments = self.payment_repo.list_payment_all()

        return [PaymentOutDTO.from_domain(payment) for payment in payments]

class ResponseListPaymentWhereMonthUseCase:
    def __init__(self, payment_repo: IPaymentRepository):
        self.payment_repo = payment_repo

    def execute(self, month: int) -> PaymentOutDTO:
        payments = self.payment_repo.response_list_payment_where_month(month)

        return [PaymentOutDTO.from_domain(payment) for payment in payments]

class ResponseListPaymentWhereYearUseCase:
    def __init__(self, payment_repo: IPaymentRepository):
        self.payment_repo = payment_repo

    def execute(self, year: int) -> PaymentOutDTO:
        payments = self.payment_repo.response_list_payment_where_year(year)

        return [PaymentOutDTO.from_domain(payment) for payment in payments]

class UpdatePaymentUsaCase:
    def __init__(self, payment_repo: IPaymentRepository):
        self.payment_repo = payment_repo

    def execute(self, dto: PaymentUpdateDTO, id: UUID) -> PaymentOutDTO:
        payment = self.payment_repo.fin_by_id(id)

        if payment is None:
            raise Exception('Pagamento não encontrado')

        if (dto.payment_method is not None):
            payment.change_payment_method(dto.payment_method)

        if (dto.status):
            payment.change_status(dto.status)

        return PaymentOutDTO.from_domain(
            self.payment_repo.save(payment)
        )
    