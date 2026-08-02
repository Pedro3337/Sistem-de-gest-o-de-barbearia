from ninja.security import HttpBearer

from users.infrasctuture.auth.jwt_service import JWTService
from users.infrasctuture.repository import UserRepository

class JWTAuth(HttpBearer):
    def __init__(self):
        super().__init__()
        self.jwt_service = JWTService()
        self.user_repo = UserRepository()

    def authenticate(self, request, token):
        payload = self.jwt_service.decode(token)

        user = self.user_repo.find_by_id(payload['sub'])

        print("TOKEN:", token)

        payload = self.jwt_service.decode(token)
        print("PAYLOAD:", payload)

        return user