from dataclasses import dataclass,field
from uuid import UUID, uuid4

from datetime import date,time

@dataclass
class CostumerServiceEntity:
    id: UUID = field(default_factory=uuid4)
    appointment: UUID = field(default=None)
    client: UUID | None = field(default=None)
    barber: UUID | None = field(default=None)
    service: UUID | None = field(default=None)
    date_a: date | None = None
    month: int = field(default=0)
    deduct: float = field(default=0)
    total_value: float = field(default=0)
    end_value: float = field(default=0)
    observation: str = field(default='')

    def change_deduct(self, deduct: float):
        self.deduct = deduct

    def change_total_value(self, total_value: float ):
        self.total_value = total_value

    def change_and_value(self, and_value: float):
        self.and_value = and_value

    def change_observation(self, observation: str):
        self.observation = observation


