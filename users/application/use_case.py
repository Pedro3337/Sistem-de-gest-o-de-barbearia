from uuid import UUID

from django.conf.locale import ro

from barber.api.schema import BarberRegisterIn
from barber.application.dtos import BarberOutDTO
from barber.domain.entities import BarberEntity
from barber.domain.repositories import IBarberRepository
from barber.infrasctuture.models import Barber
from clients.domain.entities import ClientEntity
from clients.domain.repositories import IClientRepository
from users.api.schemas import UserRegisterIn
from users.domain import role
from users.domain.entities import UserEntity
from users.domain.role import UserRole

from ..domain.repositories import IUserRepository
from .dtos import UserInDTO,UserOutDTO, UserRegisterInDTO,UserResponseDTO,UserUpdateDTO
from ..infrasctuture.auth.jwt_service import JWTService

from services.hash_service import HashPasswordService

class UserLoginUserCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo
        self.jwt = JWTService()
        self.hash_service = HashPasswordService()

    def execute(self, dto: UserInDTO, password: str) -> UserOutDTO:
        user = self.user_repo.find_by_email(dto.email)

        if not user:
            raise Exception('No user found')

        if self.hash_service.encode_password(password, user.password):
            token = self.jwt.create_access_token(user)

            # Criar hash service
            # verificar senha da requisição com o senha_hash com método do hash service
            # Se validar a senha, retorna o UserReponseDTO e o acess_token

            return UserResponseDTO(
                user=UserOutDTO.from_domain(user),
                acess_token=token
            )

class UserRegisterUseCase:
    def __init__(self, user_repo: IUserRepository, client_repo: IClientRepository):
        self.user_repo = user_repo
        self.hash_service = HashPasswordService()
        self.client_repo = client_repo

    def execute(self, dto: UserRegisterInDTO):

        if self.user_repo.very_exist_by_email(dto.email):
            raise Exception('Email already register')

        hash_password = self.hash_service.hash_password(dto.password)

        user_entity = UserEntity(
            name = dto.name,
            email = dto.email,
            password = hash_password,
            role = dto.role
        )
        user = self.user_repo.save(user_entity)

        client_entity = ClientEntity(
            user_id=user.id
        )

        self.client_repo.save(client_entity)
        
        return UserOutDTO.from_domain(user)

class UserUpdatePasswordUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo
        self.hash_service = HashPasswordService()

    def execute(self,id: UUID, new_password: str) -> UserOutDTO:
        user = self.user_repo.find_by_id(id)

        print('Senha intregue: ', new_password)

        new_password_hash = self.hash_service.hash_password(new_password)

        if not user:
            raise Exception('User not found.')

        if (new_password):
            user.change_password(new_password_hash)

        self.user_repo.save(user)
        return UserOutDTO.from_domain(user)

class RegisterBarberUseCase:
    def __init__(self, user_repo: IUserRepository, barber_repo: IBarberRepository):
        self.user_repo = user_repo
        self.barber_repo = barber_repo
        self.hash_service = HashPasswordService()

    def execute(self, dto: UserInDTO, phone: str, commission: int) -> UserOutDTO:
        if self.user_repo.very_exist_by_email(dto.email):
            raise Exception('Email already register')

        hash_password = self.hash_service.hash_password(dto.password)

        user_entity = UserEntity(
            name = dto.name,
            email = dto.email,
            password = hash_password,
            role = dto.role
        )

        user = self.user_repo.save(user_entity)

        barber_entity = BarberEntity(
            user=user.id,
            phone=phone,
            commission=commission
        )

        self.barber_repo.save(barber_entity)
        
        return UserOutDTO.from_domain(user)
    