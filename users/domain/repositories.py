from abc import ABC,abstractmethod
from uuid import UUID

from users.infrasctuture.models import User
from .entities import UserEntity

class IUserRepository(ABC):
    @abstractmethod
    def save(self, entity: UserEntity) -> UserEntity:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> UserEntity:
        ...

    @abstractmethod
    def very_exist_by_email(self, email: str) -> bool:
        ...
        
    @abstractmethod
    def find_by_id(self, id: UUID) -> UserEntity:
        ...

    @abstractmethod
    def _to_model(self, model) -> UserEntity:
        ...