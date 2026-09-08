from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from appointments.domain.role import AppointmentRole

@dataclass
class AppointmentEntity:
    id: UUID = field(default_factory=uuid4)
    client: UUID | None = field(default=None)
    barber: UUID | None = field(default=None)
    service: UUID | None = field(default=None)
    date_time: datetime = field(default_factory=datetime.now)
    status: AppointmentRole = field(default=AppointmentRole.agendado)
    observation: str = field(default='')

    def change_status(self, status: str):
        self.status = status

    def change_observation(self, observation: str):
        self.observation = observation