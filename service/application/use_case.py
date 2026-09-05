from typing import List
from uuid import UUID

from service.application.dtos import ServiceInDTO, ServiceOutDTO, ServiceUpdateDTO
from service.domain.entities import ServiceEntity
from service.domain.repositories import IServiceRepository

class RegisterServiceUseCase:
    def __init__(self, service_repo: IServiceRepository):
        self.service_repo = service_repo

    def execute(self, dto: ServiceInDTO) -> ServiceOutDTO:
        service_entity = ServiceEntity(
            name=dto.name,
            description=dto.description,
            value=dto.value,
        )

        service = self.service_repo.save(service_entity)

        return ServiceOutDTO.from_domain(service)

class ResponseServiceAllUseCase:
    def __init__(self, service_repo: IServiceRepository):
        self.service_repo = service_repo

    def execute(self) -> List[ServiceEntity]:
        services = self.service_repo.response_services_all()

        return [ServiceOutDTO.from_domain(service) for service in services]

class UpdateServiceUseCase:
    def __init__(self, service_repo: IServiceRepository):
        self.service_repo = service_repo

    def execute(self, id: UUID, dto: ServiceUpdateDTO) -> ServiceOutDTO:
        service = self.service_repo.find_by_id(id)

        print(service)

        if not service:
            raise Exception('Service not found.')

        if dto.name:
            service.change_name(dto.name)

        if dto.description:
            service.change_description(dto.description)

        if dto.duration:
            service.change_duration(dto.duration)

        if dto.value:
            service.change_value(dto.value)

        service.change_activate(dto.activate)

        return ServiceOutDTO.from_domain(self.service_repo.save(service))
        
    
        