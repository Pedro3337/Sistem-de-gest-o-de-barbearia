from typing import List
from uuid import UUID

from service.domain.entities import ServiceEntity
from service.domain.repositories import IServiceRepository
from service.infrasctuture.models import Service

class ServiceRepository(IServiceRepository):
    def save(self, entity: ServiceEntity) -> ServiceEntity:
        Service.objects.update_or_create(
            id=entity.id,
            defaults={
                'name': entity.name,
                'description': entity.description,
                'duration': entity.duration,
                'value': entity.value,
                'activate': entity.activate
            }
        )

        return entity

    def find_by_id(self, id: UUID) -> ServiceEntity:
        try:
            return self._to_model(Service.objects.get(id=id))
        except Service.DoesNotExist:
            return None

    def response_services_all(self) -> List[ServiceEntity]:
        try:
            return [self._to_model(service) for service in Service.objects.all()]
        except  Service.DoesNotExist:
            return None

    def _to_model(self, model: Service) -> ServiceEntity:
        return ServiceEntity(
            id=model.id,
            name=model.name,
            description=model.description,
            value=model.value,
            duration=model.duration,
            activate=model.activate
        )