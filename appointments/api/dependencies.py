from dependency_injector import containers,providers

from appointments.application.use_case import RegisterAppointmentUseCase, ReponseAllAppointmentUseCase, ResponseAppointmentWhereClientIdUseCase, ResponseListAppointmentWhereBarberIdAndDateUseCase, ResponseListAppointmentWhereBarberIdUseCase, UpdateAppointmentUseCase
from appointments.infracstuture.repository import AppointmentRepository

class AppointmentContainer(containers.DeclarativeContainer):
    appointment_repo = providers.Factory(
        AppointmentRepository
    )

    register_appointment_use_case = providers.Factory(
        RegisterAppointmentUseCase, appointment_repo = appointment_repo
    )

    response_all_appointment = providers.Factory(
        ReponseAllAppointmentUseCase, appointment_repo = appointment_repo
    )

    response_appointment_where_barber_id = providers.Factory(
        ResponseListAppointmentWhereBarberIdUseCase, appointment_repo = appointment_repo
    )

    response_appointment_where_barber_id_and_date = providers.Factory(
        ResponseListAppointmentWhereBarberIdAndDateUseCase, appointment_repo = appointment_repo
    )

    response_appointment_where_client_id = providers.Factory(
        ResponseAppointmentWhereClientIdUseCase, appointment_repo = appointment_repo
    )

    update_appointment_use_case = providers.Factory(
        UpdateAppointmentUseCase, appointment_repo = appointment_repo
    )