from dataclasses import dataclass,field
from uuid import UUID, uuid4

from users.domain.role import UserRole

@dataclass
class UserEntity:
    id: UUID = field(default_factory=uuid4)
    name: str = field(default='')
    email: str = field(default='')
    password: str = field(default='')
    role: UserRole = field(default=UserRole.cliente)
    activate: bool = field(default=True)

    def change_name(self, name):
        self.name = name

    def change_email(self, email):
        self.email = email

    def change_password(self, password):
        self.password = password

    def change_activate(self, activate):
        self.activate = activate