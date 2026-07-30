from abc import ABC,abstractmethod
from uuid import UUID

from clients.domain.entities import ClientEntity

class IClientRepository(ABC):
    @abstractmethod
    def save(self, entity: ClientEntity) -> ClientEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> ClientEntity:
        ...

    @abstractmethod
    def _to_model(self, model) -> ClientEntity:
        ...
    