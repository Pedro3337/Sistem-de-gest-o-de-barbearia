from uuid import UUID, uuid4

from ninja import Schema

from users.domain.role import UserRole
from ..application.dtos import UserInDTO,UserOutDTO, UserRegisterInDTO, UserResponseDTO,UserUpdateDTO

class UserIn(Schema):
    email: str

    def to_dto(self) -> UserInDTO:
        return UserInDTO(
            email=self.email,
        )

class UserRegisterIn(Schema):
    name: str
    email: str
    password: str

    def to_dto(self):
        return UserRegisterInDTO(
            name = self.name,
            email = self.email,
            password = self.password,
        )

class UserOut(Schema):
    id: UUID
    name: str
    email: str
    role: UserRole
    activate: bool

    @classmethod
    def from_domain(self, dto: UserOutDTO):
        return UserOut(
            id = str(dto.id),
            name = dto.name,
            email = dto.email,
            role = dto.role,
            activate=dto.activate
        )

class UserUpdate(Schema):
    id: UUID | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None
    activate: bool | None = None

    def to_dto(self) -> UserUpdateDTO:
        return UserUpdateDTO(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password,
            activate=self.activate
        )