from abc import ABC,abstractmethod
from .entities import UserEntity

class IUserRepository(ABC):
    @abstractmethod
    def find_by_email_and_possword(email: str, possword: str) -> UserEntity:
        ...