from uuid import UUID

from pydantic import  BaseModel

from users.domain.entities import UserEntity
from users.domain.role import UserRole

class UserInDTO(BaseModel):
    email: str

class UserOutDTO(BaseModel):
    id: UUID
    name: str
    email: str
    role: UserRole
    activate: bool

    @classmethod
    def from_domain(cls, entity: UserEntity):
        return cls(
            id = str(entity.id),
            name = entity.name,
            email = entity.email,
            role = entity.role,
            activate = entity.activate
        )

class UserResponseDTO(BaseModel):
    user: UserOutDTO
    acess_token: str

class UserRegisterInDTO(BaseModel):
    name: str
    email: str
    password: str

class UserUpdateDTO(BaseModel):
    id: UUID | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None
    activate: bool | None = None

