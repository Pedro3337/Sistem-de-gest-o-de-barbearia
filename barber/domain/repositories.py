from abc import ABC,abstractmethod
from typing import List
from uuid import UUID

from barber.domain.entities import BarberEntity
from barber.infrasctuture.models import Barber

class IBarberRepository(ABC):
    @abstractmethod
    def save(self, entity: BarberEntity) -> BarberEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> BarberEntity:
        ...

    @abstractmethod
    def list_all_barber(self) -> List[BarberEntity]:
        ...

    @abstractmethod
    def _to_model(self, model: Barber) -> BarberEntity:
        ...