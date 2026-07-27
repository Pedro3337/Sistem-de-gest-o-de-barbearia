from uuid import UUID, uuid4

from ninja import Schema
from ..application.dtos import UserInDTO,UserOutDTO, UserResponseDTO,UserUpdateDTO

class UserIn(Schema):
    email: str
    passowrd: str

    def to_dto(self) -> UserInDTO:
        return UserInDTO(
            email=self.email,
            password=self.passowrd
        )

class UserOut(Schema):
    id: UUID
    name: str
    email: str

    @classmethod
    def from_domain(self, dto: UserOutDTO):
        return UserOut(
            id = str(dto.id),
            name = dto.name,
            email = dto.email,
        )

class UserUpdate(Schema):
    id: UUID | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None

    def to_dto(self) -> UserUpdateDTO:
        return UserUpdateDTO(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password
        )