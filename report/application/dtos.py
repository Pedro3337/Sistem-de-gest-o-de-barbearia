from pydantic import BaseModel


class DashboardInDTO(BaseModel):
    year: int
    mounth: int

class MostFrequentlyPerformedServiceDTO(BaseModel):
    name: str
    amount: int

class DashboardOutDTO(BaseModel):
    monthly_revenue: float
    annual_revenue: float
    total_services_provided: int
    clients_served: int
    most_frequently_provided_service: MostFrequentlyPerformedServiceDTO

class DashboardBarberOutDTO(BaseModel):
    costumer_service_mount: int
    invoiced_amount: float
    invoiced_amount_today: float
