from dependency_injector import containers,providers

from appointments.application.use_cases import RegisterAppointmentUseCase, ResponseAllAppointmentUseCase, ResponseAppointmentWhereClientIdUseCase, ResponseListAppointmentWhereBarberIdAndDateUseCase, ResponseListAppointmentWhereBarberIdUseCase, UpdateAppointmentUseCase
from appointments.infracstuture.repository import AppointmentRepository
from barber.application.use_case import ResponseAllBarberUseCase

class AppointmentContainer(containers.DeclarativeContainer):
    appointment_repo = providers.Factory(AppointmentRepository)

    register_appointment_repo = providers.Factory(
        RegisterAppointmentUseCase,  appointment_repo = appointment_repo
    )

    response_all_appointments_use_case = providers.Factory(
        ResponseAllAppointmentUseCase, appointment_repo = appointment_repo
    )

    response_list_appointment_where_barber_id_use_case = providers.Factory(
        ResponseListAppointmentWhereBarberIdUseCase, appointment_repo = appointment_repo
    )

    response_appointment_where_client_id = providers.Factory(
        ResponseAppointmentWhereClientIdUseCase, appointment_repo = appointment_repo
    )

    response_list_appointment_where_barber_id_and_date_use_case = providers.Factory(
        ResponseListAppointmentWhereBarberIdAndDateUseCase, appointment_repo = appointment_repo
    )



    update_apointment_use_case = providers.Factory(
        UpdateAppointmentUseCase , appointment_repo = appointment_repo
    )