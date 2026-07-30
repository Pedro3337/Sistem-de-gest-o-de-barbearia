from dependency_injector import providers, containers

from clients.application.use_case import RegisterClientUseCase
from clients.infrasctuture.repository import ClienteRepository

class ClientContainer(containers.DeclarativeContainer):
    client_repo = providers.Factory(ClienteRepository)

    register_client_use_case = providers.Factory(
        RegisterClientUseCase,
        client_repo = client_repo
    )