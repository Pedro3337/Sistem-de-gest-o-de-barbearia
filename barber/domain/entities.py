from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class BarberEntity:
    id: int = field(default_factory=uuid4)
    user: UUID = field(default=None)
    phone: str = field(default='')
    commission: int =  field(default=0)
    activate: bool = field(default=False)

    def change_phone(self, phone):
        self.phone = phone

    def change_comission(self, commission):
        self.commission = commission

    def change_activate(self, activate):
        self.activate = activate


    