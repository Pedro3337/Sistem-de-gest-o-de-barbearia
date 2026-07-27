from turtle import st
from uuid import UUID

from pydantic import  BaseModel

from users.domain.entities import UserEntity

class UserInDTO(BaseModel):
    email: str
    password: str

class UserOutDTO(BaseModel):
    id: UUID
    name: str
    email: str

    @classmethod
    def from_domain(cls, entity: UserEntity):
        return cls(
            id = str(entity.id),
            name = entity.name,
            email = entity.email,
        )

class UserResponseDTO(BaseModel):
    user: UserOutDTO
    acess_token: str

class UserUpdateDTO(BaseModel):
    id: UUID | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None