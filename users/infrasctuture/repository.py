from uuid import UUID

from ..domain.repositories import IUserRepository
from ..domain.entities import UserEntity
from .models import User

class UserRepository(IUserRepository):
    def save(self, entity: UserEntity) -> UserEntity:
        User.objects.update_or_create(
            id=entity.id,
            defaults={
                'email': entity.email,
                'password': entity.password,
            }
        )

        return entity

    def find_by_email(self,email: str) -> UserEntity:
        try:
            user = User.objects.get(email=email)
            return self._to_model(user)
        except User.DoesNotExist:
            return None

    def find_by_id(self, id: UUID) -> UserEntity:
        try:
            return self._to_model(User.objects.get(id=id))
        except User.DoesNotExist:
            return None

    def _to_model(self, model) -> UserEntity:
        return UserEntity(
            id=model.id,
            name=model.name,
            email=model.email,
            password=model.password
        )