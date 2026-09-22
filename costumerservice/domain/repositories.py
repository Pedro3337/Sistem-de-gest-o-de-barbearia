from abc import ABC,abstractmethod
from typing import List
from uuid import UUID

from costumerservice.domain.entities import CostumerServiceEntity
from costumerservice.infracstuture.models import CostumerService

class ICostumerServiceRepository(ABC):
    @abstractmethod
    def save(self, entity: CostumerServiceEntity) -> CostumerServiceEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> CostumerServiceEntity:
        ...

    @abstractmethod
    def response_all_costumer_service(self) -> List[CostumerServiceEntity]:
        ...

    @abstractmethod
    def response_costumer_service_where_month(self) -> List[CostumerServiceEntity]:
        ...

    @abstractmethod
    def response_costumer_service_where_barber_id_and_month(self) -> List[CostumerServiceEntity]:
        ...

    @abstractmethod
    def response_costumer_service_where_date(self) -> List[CostumerServiceEntity]:
        ...

    @abstractmethod
    def response_costumer_service_where_barber_id_and_date(self) -> List[CostumerServiceEntity]:
        ...

    @abstractmethod
    def _to_model(self, model=CostumerService) -> CostumerServiceEntity:
        ...