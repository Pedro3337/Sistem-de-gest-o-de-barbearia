from abc import ABC,abstractmethod
from uuid import UUID
from .entities import UserEntity

class IUserRepository(ABC):
    @abstractmethod
    def save(self, entity: UserEntity) -> UserEntity:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> UserEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> UserEntity:
        ...

    @abstractmethod
    def _to_model(self, model) -> UserEntity:
        ...