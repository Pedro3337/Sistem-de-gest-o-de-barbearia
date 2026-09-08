from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from uuid import UUID

from appointments.domain.entities import AppointmentEntity
from appointments.infracstuture.models import Appointments

class IAppointmentsRepository(ABC):
    @abstractmethod
    def save(self, enity: AppointmentEntity) -> AppointmentEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> AppointmentEntity:
        ...

    @abstractmethod
    def response_all_appointments(self) -> List[AppointmentEntity]:
        ...

    @abstractmethod
    def response_appointments_where_barber_id(self, barber_UUID: UUID) -> List[AppointmentEntity]:
        ...

    @abstractmethod
    def response_appointment_where_client_id(self, client_id: UUID) -> AppointmentEntity:
        ...

    @abstractmethod
    def response_appointement_where_barber_id_and_date(self, id: UUID, date: datetime) -> List[AppointmentEntity]:
        ...

    @abstractmethod
    def _to_model(self, model: Appointments):
        ...

    