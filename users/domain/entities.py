from dataclasses import dataclass,field
from uuid import UUID, uuid4

@dataclass
class UserEntity:
    id: UUID = field(default_factory=uuid4)
    name: str = field(default='')
    email: str = field(default='')
    password: str = field(default='')

    def change_name(self, name):
        self.name = name

    def change_email(self, email):
        self.email = email

    def change_passord(self, password):
        self.password = password