from abc import ABC,abstractmethod
from uuid import UUID

from typing import List

from service.domain.entities import ServiceEntity

class IServiceRepository(ABC):
    @abstractmethod
    def save(self, entity:ServiceEntity ) -> ServiceEntity:
        ...

    def find_by_id(self, id: UUID):
        ...

    def response_services_all(self) -> List[ServiceEntity]:
        ...

    def _to_model(self, model: ServiceEntity) -> ServiceEntity:
        ...