from uuid import UUID

from clients.domain.entities import ClientEntity
from clients.domain.repositories import IClientRepository
from clients.infrasctuture.models import Client
from users.infrasctuture.models import User

class ClienteRepository(IClientRepository):
    def save(self, entity: ClientEntity) -> ClientEntity:

        user = User.objects.get(id=entity.user_id)

        Client.objects.create(user=user)

        return entity

    def find_by_id(self, id: UUID) -> ClientEntity:
        try:
            return self._to_model(Client.objects.get(id=id))
        except Client.DoesNotExist:
            return None

    def _to_model(self, model):
        return ClientEntity(
            id=model.id,
            user_id=model.user_id,
            date_register=model.date_register
        )
    