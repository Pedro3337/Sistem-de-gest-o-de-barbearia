from datetime import datetime
from typing import List
from uuid import UUID

from appointments.api.schemas import AppointmentUpdateDTO
from appointments.application.dtos import AppointmentInDTO, AppointmentOutDTO
from appointments.domain.entities import AppointmentEntity
from appointments.domain.repositories import IAppointmentsRepository

class RegisterAppointmentUseCase:
    def __init__(self, appointment_repo: IAppointmentsRepository):
        self.appointment_repo = appointment_repo

    def execute(self, dto: AppointmentInDTO) -> AppointmentOutDTO:
        appointment_entity = AppointmentEntity(
            client=dto.client,
            barber=dto.barber,
            service=dto.service,
            date_time=dto.date_time,
            status=dto.status,
            observation=dto.observation
        )

        appointment = self.appointment_repo.save(appointment_entity)

        return AppointmentOutDTO.from_domain(appointment)

class ReponseAllAppointmentUseCase:
    def __init__(self, appointment_repo: IAppointmentsRepository):
        self.appointment_repo = appointment_repo

    def execute(self) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_all_appointments()

        return [
            AppointmentOutDTO.from_domain(appointment)
            for appointment in appointments
        ]

class ResponseListAppointmentWhereBarberIdUseCase:
    def __init__(self, appointment_repo: IAppointmentsRepository):
        self.appointment_repo = appointment_repo

    def execute(self, barber_UUID: UUID) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_appointments_where_barber_id(barber_UUID)

        return [
            AppointmentOutDTO.from_domain(appointment)
            for appointment in appointments
        ]

class ResponseListAppointmentWhereBarberIdAndDateUseCase:
    def __init__(self, appointment_repo: IAppointmentsRepository):
        self.appointment_repo = appointment_repo

    def execute(self, id: UUID, date: datetime) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_appointement_where_barber_id_and_date(id, date)

        return [
            AppointmentOutDTO.from_domain(appointment)
            for appointment in appointments
        ]

class ResponseAppointmentWhereClientIdUseCase:
    def __init__(self, appointment_repo: IAppointmentsRepository):
        self.appointment_repo = appointment_repo

    def execute(self, client_UUID: UUID) -> List[AppointmentOutDTO]:

        appointment = self.appointment_repo.response_appointment_where_client_id(client_UUID)

        return AppointmentOutDTO.from_domain(appointment)

class UpdateAppointmentUseCase:
    def __init__(self, appointment_repo: IAppointmentsRepository):
        self.appointment_repo = appointment_repo

    def execute(self, dto: AppointmentUpdateDTO, id: UUID) -> AppointmentOutDTO:
        appointment = self.appointment_repo.find_by_id(id)

        appointment.change_status(dto.status)

        if (dto.observation):
            appointment.change_observation(dto.observation)

        return AppointmentOutDTO.from_domain(self.appointment_repo.save(appointment))
