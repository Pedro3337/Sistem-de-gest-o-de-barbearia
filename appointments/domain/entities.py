from dataclasses import dataclass,field
from datetime import date,time
from uuid import UUID, uuid4

from appointments.application.role import AppointmentRole

@dataclass
class AppointmentEntity:
    id: UUID = field(default_factory=uuid4)
    client: UUID | None = field(default=None)
    barber: UUID | None = field(default=None)
    service: UUID | None = field(default=None)
    date_a: date = field(default_factory=date)
    time_a: time = field(default_factory=time)
    status: AppointmentRole = field(default=AppointmentRole.agendado)
    observation: str = field(default='')

    def change_status(self, status: AppointmentRole) -> None:
        self.status = status

    def change_observation(self, observation: str) -> None:
        self.observation = observation

        