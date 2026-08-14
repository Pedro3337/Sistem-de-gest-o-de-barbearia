from uuid import UUID

from pydantic import BaseModel

from barber.domain.entities import BarberEntity
from users.domain.role import UserRole


class BarberRegisterInDTO(BaseModel):
    name: str
    email: str
    password: str
    role: UserRole
    phone: str
    commission: int

class BarberOutDTO(BaseModel):
    id: UUID
    user: UUID
    phone: str
    commission: int
    activate: bool

    @classmethod
    def from_domain(self, entity: BarberEntity):
        return BarberOutDTO(
            id = entity.id,
            user = entity.user.id,
            phone = entity.phone,
            commission = entity.commission,
            activate = entity.activate
        )

class BarberUpdateDTO(BaseModel):
    phone: str | None = None
    commission: int | None = None
    activate: bool | None = None