from ...domain.entities import UserEntity
import jwt
from datetime import datetime,timedelta

from django.conf import settings

class JWTService:

    MY_SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = 'HS256'

    def create_access_token(self, user: UserEntity) -> str:
        try:
            payload = {
                'sub': str(user.id),
                'email': user.email,
                'role': user.role,
                'exp': datetime.utcnow() + timedelta(minutes=30),
            }

            token = jwt.encode(
                payload,
                self.MY_SECRET_KEY,
                algorithm=self.ALGORITHM
            )

            return token
        except:
            raise Exception('Error')

    def create_refresh_token(self, user: UserEntity) -> str:
        ...

    def decode(self, token: str):
        payload = jwt.decode(
            token,
            self.MY_SECRET_KEY,
            algorithms=[self.ALGORITHM]
        )

        return payload