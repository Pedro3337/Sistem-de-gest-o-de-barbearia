from dependency_injector import containers, providers

from payment.application.use_cases import RegisterPaymentUseCase, ResponseListAllPaymentUseCase, ResponseListPaymentWhereMonthUseCase, ResponseListPaymentWhereYearUseCase, UpdatePaymentUsaCase
from payment.infracstuture.repository import PaymentRepository

class PaymentContainer(containers.DeclarativeContainer):
    payment_repo = providers.Factory(
        PaymentRepository
    )

    register_payment_use_case = providers.Factory(
        RegisterPaymentUseCase, payment_repo = payment_repo
    )

    response_list_all_use_case = providers.Factory(
        ResponseListAllPaymentUseCase, payment_repo = payment_repo
    )

    response_list_payment_where_month_use_case = providers.Factory(
        ResponseListPaymentWhereMonthUseCase, payment_repo = payment_repo
    )

    response_list_payment_where_year_use_case = providers.Factory(
        ResponseListPaymentWhereYearUseCase, payment_repo = payment_repo
    )

    update_payment_use_case = providers.Factory(
        UpdatePaymentUsaCase, payment_repo = payment_repo
    )