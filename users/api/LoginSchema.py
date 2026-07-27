from ninja import Schema

from users.api.schemas import UserOut
from users.application.dtos import UserResponseDTO

class LoginResponse(Schema):
    user: UserOut
    acess_token: str

    @classmethod
    def from_domain(cls, dto: UserResponseDTO):
        return LoginResponse(
            user = UserOut.from_domain(dto.user),
            acess_token = dto.acess_token
        )