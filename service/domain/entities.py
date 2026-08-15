from dataclasses import dataclass,field
from uuid import UUID, uuid4

from django.utils.timezone import activate

@dataclass
class ServiceEntity:
    id: UUID = field(default_factory=uuid4)
    name: str = field(default='')
    description: str = field(default='')
    duration: int = field(default=0)
    value: float = field(default=0)
    activate: bool = field(default=True)

    def change_name(self, name: str):
        self.name = name

    def change_description(self, description: str):
        self.description = description

    def change_duration(self, duration: int):
        self.duration = duration

    def change_value(self, value: float):
        self.value = value

    def change_activate(self, activate: bool):
        self.description = activate