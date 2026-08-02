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
    name: str
    email: str
    role: UserRole
    activate: bool
    phone: str
    commission: int

    @classmethod
    def from_domain(self, entity: BarberEntity):
        return BarberOutDTO(
            id = str(entity.id),
            name = entity.name,
            email = entity.email,
            role = entity.role,
            activate = entity.activate,
            phone = entity.phone,
            commission = entity.commission
        )
