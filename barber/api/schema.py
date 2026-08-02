from uuid import UUID

from ninja import Schema

from barber.application.dtos import BarberOutDTO, BarberRegisterInDTO
from barber.infrasctuture.models import Barber
from users.domain.role import UserRole

class BarberRegisterIn(Schema):
    phone: str
    commission: int

    def to_dto(self):
        return BarberRegisterInDTO(
            name = self.name,
            email = self.email,
            password = self.password,
            role = self.role,
            phone=self.phone,
            commission=self.commission
        )



class BarberOut(Schema):
    id: UUID
    name: str
    email: str
    role: UserRole
    activate: bool
    phone: str
    commission: int

    @classmethod
    def from_domain(self, dto: BarberOutDTO):
        return BarberOut(
            id = str(dto.id),
            name = dto.name,
            email = dto.email,
            role = dto.role,
            activate = dto.activate,
            phone = dto.phone,
            commission = dto.commission
        )



class BarberUpdate(Schema):
    id: UUID | None = None
    user_id: UUID | None = None
    telefone: str | None = None
    commission: float | None = None
    activate: bool | None = None