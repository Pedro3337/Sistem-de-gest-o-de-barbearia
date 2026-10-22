from ninja import Schema

from report.application.dtos import DashboardBarberOutDTO, DashboardInDTO, DashboardOutDTO, MostFrequentlyPerformedServiceDTO

class DashboardIn(Schema):
    year: int
    mounth: int

    def to_dto(self) -> DashboardInDTO:
        return DashboardInDTO(
            year=self.year,
            mounth=self.mounth,
        )

class MostFrequentlyPerformedService(Schema):
    name: str
    amount: int

    @classmethod
    def from_domain(cls, dto: MostFrequentlyPerformedServiceDTO):
        return cls(
            name=dto.name,
            amount=dto.amount
        )

class DashboardOut(Schema):
    monthly_revenue: float
    annual_revenue: float
    total_services_provided: int
    clients_served: int
    most_frequently_provided_service: MostFrequentlyPerformedService

    @classmethod
    def from_domain(cls, dto: DashboardOutDTO):
        return cls(
            monthly_revenue = dto.monthly_revenue,
            annual_revenue = dto.annual_revenue,
            total_services_provided = dto.total_services_provided,
            clients_served = dto.clients_served,
            most_frequently_provided_service = MostFrequentlyPerformedService.from_domain(dto.most_frequently_provided_service)
        )

class DashboardBarberOut(Schema):
    costumer_service_mount: int
    invoiced_amount: float
    invoiced_amount_today: float

    @classmethod
    def from_domain(cls, dto: DashboardBarberOutDTO):
        return cls(
            costumer_service_mount = dto.costumer_service_mount,
            invoiced_amount = dto.invoiced_amount,
            invoiced_amount_today = dto.invoiced_amount_today
        )