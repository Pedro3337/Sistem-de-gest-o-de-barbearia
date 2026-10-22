from dependency_injector import containers, providers

from costumerservice.infracstuture.repository import CostumerServiceRepository
from payment.infracstuture.repository import PaymentRepository
from report.application.use_cases import ResponseReportBarberUseCase, ResponseReportUseCase

class ReportContainer(containers.DeclarativeContainer):
    payment_repo = providers.Factory(PaymentRepository)
    costumer_service_repo = providers.Factory(CostumerServiceRepository)

    response_report_use_case = providers.Factory(
        ResponseReportUseCase, payment_repo = payment_repo, costumer_service_repo = costumer_service_repo
    )

    response_report_barber_use_case = providers.Factory(
        ResponseReportBarberUseCase, payment_repo = payment_repo, costumer_service_repo = costumer_service_repo
    )