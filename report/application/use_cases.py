from collections import Counter
from datetime import date
from uuid import UUID

from costumerservice.domain.repositories import ICostumerServiceRepository
from costumerservice.infracstuture.models import CostumerService
from payment.domain.repositories import IPaymentRepository
from report.application.dtos import DashboardBarberOutDTO, DashboardInDTO, DashboardOutDTO, MostFrequentlyPerformedServiceDTO


class ResponseReportUseCase:
    def __init__(self, payment_repo: IPaymentRepository, costumer_service_repo: ICostumerServiceRepository):
        self.payment_repo = payment_repo
        self.costumer_service_repo = costumer_service_repo

    def execute(self, year: int, month: int):

        payments_month = (self.payment_repo.response_list_payment_where_month(month))
        payments_year = (self.payment_repo.response_list_payment_where_year(year))

        payments_month_quant = sum(payment.value for payment in payments_month)
        payments_year_quant = sum(payment.value for payment in payments_year)

        costumerservices = self.costumer_service_repo.response_costumer_service_where_month(month)

        total_costumerservices = len(costumerservices)

        clients_serverd = len({
            costumerservice.client for costumerservice in costumerservices
        })

        costumer_services_orm = CostumerService.objects.filter(month=month)

        amount_per_serving = Counter(
            costumerservice.service.name for costumerservice in costumer_services_orm
        )

        if amount_per_serving:
            service,amount = amount_per_serving.most_common(1)[0]
        else:
            service = None
            amount = 0

        return DashboardOutDTO(
            monthly_revenue=payments_month_quant,
            annual_revenue=payments_year_quant,
            total_services_provided=total_costumerservices,
            clients_served=clients_serverd,
            most_frequently_provided_service=MostFrequentlyPerformedServiceDTO(
                name=service,
                amount=amount
            )
        )

class ResponseReportBarberUseCase:
    def __init__(self, payment_repo: IPaymentRepository, costumer_service_repo: ICostumerServiceRepository):
        self.payment_repo = payment_repo
        self.costumer_service_repo = costumer_service_repo

    def execute(self, id: UUID, month: int, date: date):
        costumer_services = self.costumer_service_repo.response_costumer_service_where_barber_id_and_month(id, month)
        costumer_services_today = self.costumer_service_repo.response_costumer_service_where_barber_id_and_date(id, date)
        
        costumer_services_mount = len(costumer_services)

        valor_faturado = sum(
            costumer_service.end_value for costumer_service in costumer_services
        )

        valor_faturado_hoje = sum(
            costumer_service.end_value for costumer_service in costumer_services_today
        )


        return DashboardBarberOutDTO(
            costumer_service_mount = costumer_services_mount,
            invoiced_amount = valor_faturado,
            invoiced_amount_today = valor_faturado_hoje
        )
