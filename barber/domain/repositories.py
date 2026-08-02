from abc import ABC,abstractmethod
from uuid import UUID

from barber.domain.entities import BarberEntity

class IBarberRepository(ABC):
    @classmethod
    def save(self, entity: BarberEntity) -> BarberEntity:
        ...
