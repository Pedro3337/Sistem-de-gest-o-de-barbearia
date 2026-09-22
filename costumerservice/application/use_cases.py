from datetime import date
from typing import List
from uuid import UUID

from costumerservice.application.dtos import ConstumerServiceUpdateDTO, CostumerServiceInDTO, CostumerServiceOutDTO
from costumerservice.domain.entities import CostumerServiceEntity
from costumerservice.domain.repositories import ICostumerServiceRepository


class RegisterCostumerServiceUseCase:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self, dto: CostumerServiceInDTO) -> CostumerServiceOutDTO:
        costumer_service_entity = CostumerServiceEntity(
            appointment=dto.appointment,
            client=dto.client,
            barber=dto.barber,
            service=dto.service,
            date_a=dto.date_a,
            month=dto.month,
            deduct=dto.deduct,
            total_value=dto.total_value,
            end_value=dto.total_value - (dto.total_value * (dto.deduct/100)),
            observation=dto.observation
        )

        return CostumerServiceOutDTO.from_domain(self.costumer_service_repo.save(costumer_service_entity))

class ResponseAllCostumerServiceUseCase:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self) -> List[CostumerServiceOutDTO]:
        costumer_services = self.costumer_service_repo.response_all_costumer_service()

        return [CostumerServiceOutDTO.from_domain(costumer_service) for costumer_service in costumer_services]

class ResponseCostumerServiceWhereMonth:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self, month: int) -> List[CostumerServiceOutDTO]:
        costumer_services = self.costumer_service_repo.response_costumer_service_where_month(month)

        return [CostumerServiceOutDTO.from_domain(costumer_service) for costumer_service in costumer_services]

class ResponseCostumerServiceWhereBarberIdAndMonth:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self,barber: UUID, month: int) -> List[CostumerServiceOutDTO]:
        costumer_services = self.costumer_service_repo.response_all_costumer_service(barber, month)

        return [CostumerServiceOutDTO.from_domain(costumer_service) for costumer_service in costumer_services]

class ResponseCostumerServiceWhereDate:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self, date: date) -> List[CostumerServiceOutDTO]:
        costumer_services = self.costumer_service_repo.response_costumer_service_where_date(date)

        return [CostumerServiceOutDTO.from_domain(costumer_service) for costumer_service in costumer_services]

class ResponseCostumerServiceWhereBarberIdAndDate:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self, barber: UUID, date: int) -> List[CostumerServiceOutDTO]:
        costumer_services = self.costumer_service_repo.response_costumer_service_where_barber_id_and_date(barber, date)

        return [CostumerServiceOutDTO.from_domain(costumer_service) for costumer_service in costumer_services]

class UpdateCostumerServiceUseCase:
    def __init__(self, costumer_service_repo: ICostumerServiceRepository):
        self.costumer_service_repo = costumer_service_repo

    def execute(self, dto: ConstumerServiceUpdateDTO, id: UUID) -> CostumerServiceOutDTO:
        costumer_service = self.costumer_service_repo.find_by_id(id)

        if (dto.deduct):
            costumer_service.change_deduct(dto.deduct)

        if (dto.total_value):
            costumer_service.change_total_value(dto.total_value)

        if (dto.end_value):
            costumer_service.change_and_value(dto.end_value)

        if (dto.observation):
            costumer_service.change_observation(dto.observation)

        return CostumerServiceOutDTO.from_domain(self.costumer_service_repo.save(costumer_service))