from clients.application.dtos import ClientInDTO, ClientOutDTO
from clients.domain.entities import ClientEntity
from clients.domain.repositories import IClientRepository


class RegisterClientUseCase:
    def __init__(self, client_repo: IClientRepository):
        self.client_repo = client_repo
        

    def execute(self, dto: ClientInDTO) -> ClientOutDTO:
        client = ClientEntity(
            user_id=dto.user_id
        )

        self.client_repo.save(client)
        return ClientOutDTO.from_domain(client)