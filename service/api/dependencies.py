from dependency_injector import containers, providers

from service.application.use_case import RegisterServiceUseCase, ResponseServiceAllUseCase, UpdateServiceUseCase
from service.infrasctuture.repository import ServiceRepository

class ServiceContainer(containers.DeclarativeContainer):
    service_repo = providers.Factory(ServiceRepository)

    register_service_use_case = providers.Factory(
        RegisterServiceUseCase, service_repo = service_repo
    )

    response_all_services_use_case = providers.Factory(
        ResponseServiceAllUseCase, service_repo = service_repo
    )

    update_service_use_case = providers.Factory(
        UpdateServiceUseCase, service_repo = service_repo
    )