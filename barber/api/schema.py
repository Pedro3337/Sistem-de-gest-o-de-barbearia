from uuid import UUID

from ninja import Schema

from barber.application.dtos import BarberOutDTO, BarberRegisterInDTO, BarberUpdateDTO
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
    user: UUID
    phone: str
    commission: int
    activate: bool

    @classmethod
    def from_domain(self, dto: BarberOutDTO):
        return BarberOut(
            id = dto.id,
            user = dto.user,
            phone = dto.phone,
            commission = dto.commission,
            activate = dto.activate
        )



class BarberUpdate(Schema):
    phone: str | None = None
    commission: float | None = None
    activate: bool | None = None

    def to_dto(self):
        return BarberUpdateDTO(
            phone=self.phone,
            commission=self.commission,
            activate=self.activate
        )