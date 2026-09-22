from datetime import date
from typing import List
from uuid import UUID

from appointments.application.dtos import AppointmentInDTO, AppointmentOutDTO, AppointmentUpdateDTO
from appointments.domain.entities import AppointmentEntity
from appointments.domain.respositorie import IAppointmentRepositorie


class RegisterAppointmentUseCase:
    def __init__(self, appointment_repo: IAppointmentRepositorie):
        self.appointment_repo = appointment_repo

    def execute(self, dto: AppointmentInDTO) -> AppointmentOutDTO:
        appointment_entity = AppointmentEntity(
            client=dto.client,
            barber=dto.barber,
            service=dto.service,
            date_a=dto.date_a,
            time_a=dto.time_a,
            status=dto.status,
            observation=dto.observation
        )

        appointment = self.appointment_repo.save(appointment_entity)

        return AppointmentOutDTO.from_domain(appointment)

class ResponseAllAppointmentUseCase:
    def __init__(self, appointment_repo: IAppointmentRepositorie):
        self.appointment_repo = appointment_repo

    def execute(self) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_all_appointments()

        return [
            AppointmentOutDTO.from_domain(appointment)
            for appointment in appointments
        ]

class ResponseListAppointmentWhereBarberIdUseCase:
    def __init__(self, appointment_repo: IAppointmentRepositorie):
        self.appointment_repo = appointment_repo

    def execute(self, barber_UUID: UUID) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_appointments_where_barber_id(barber_UUID)

        return [
            AppointmentOutDTO.from_domain(appointment)
            for appointment in appointments
        ]

class ResponseListAppointmentWhereBarberIdAndDateUseCase:
    def __init__(self, appointment_repo: IAppointmentRepositorie):
        self.appointment_repo = appointment_repo

    def execute(self, id: UUID, date: date) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_appointement_where_barber_id_and_date(id, date)

        return [
            AppointmentOutDTO.from_domain(appointment)
            for appointment in appointments
        ]

class ResponseAppointmentWhereClientIdUseCase:
    def __init__(self, appointment_repo: IAppointmentRepositorie):
        self.appointment_repo = appointment_repo

    def execute(self, id: UUID) -> List[AppointmentOutDTO]:

        appointments = self.appointment_repo.response_appointment_where_client_id(id)

        return [AppointmentOutDTO.from_domain(appointment) for appointment in appointments]

class UpdateAppointmentUseCase:
    def __init__(self, appointment_repo: IAppointmentRepositorie):
        self.appointment_repo = appointment_repo

    def execute(self, dto: AppointmentUpdateDTO, id: UUID) -> AppointmentOutDTO:
        appointment = self.appointment_repo.find_by_id(id)

        if (dto.status):
            appointment.change_status(dto.status)

        if (dto.observation):
            appointment.change_observation(dto.observation)

        new_appointment = self.appointment_repo.save(appointment)

        return AppointmentOutDTO.from_domain(new_appointment)