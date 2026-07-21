from ..domain.repositories import IUserRepository
from ..application.dtos import UserInDTO,UserOutDTO,UserResponseDTO,UserUpdateDTO
from ..infrasctuture.auth.jwt_service import JWTService

class UserLoginUserCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo
        self.jwt = JWTService()

    def execute(self, dto: UserInDTO) -> UserOutDTO:
        user = self.user_repo.find_by_email_and_password(dto.email,dto.password)

        if not user:
            ...

        token = self.jwt.create_acess_token(user)

        return UserOutDTO(
            user=user,
            acess_token=token
        )