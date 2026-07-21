from .repositories import IUserRepository
from .entities import UserEntity
from ..models import User

class UserRepository(IUserRepository):
    def save(self):
        pass

    def find_by_email_and_possword(self,email: str, password: str) -> UserEntity:
        try:
            user = User.objects.get(email=email,password=password)
            return self._to_model(user)
        except User.DoesNotExist:
            None

    def _to_model(self,model) -> UserEntity:
        return UserEntity(
            id=model.id,
            name=model.name,
            email=model.email,
            password=model.password
        )