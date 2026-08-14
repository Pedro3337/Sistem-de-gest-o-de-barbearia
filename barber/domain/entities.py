from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class BarberEntity:
    id: UUID = field(default_factory=uuid4)
    user: UUID | None = field(default=None)
    phone: str = field(default='')
    commission: int =  field(default=0)
    activate: bool = field(default=False)

    def change_user(self, user: UUID):
        self.user = user

    def change_phone(self, phone):
        self.phone = phone

    def change_comission(self, commission: int):
        self.commission = commission

    def change_activate(self, activate: bool):
        self.activate = activate


    