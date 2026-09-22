from dependency_injector import containers, providers

from appointments.application.use_cases import ResponseAllAppointmentUseCase
from costumerservice.application.use_cases import RegisterCostumerServiceUseCase, ResponseAllCostumerServiceUseCase, ResponseCostumerServiceWhereBarberIdAndDate, ResponseCostumerServiceWhereBarberIdAndMonth, ResponseCostumerServiceWhereDate, ResponseCostumerServiceWhereMonth, UpdateCostumerServiceUseCase
from costumerservice.infracstuture.repository import CostumerServiceRepository

class CostumerServiceContainer(containers.DeclarativeContainer):
    costumer_service_repo = providers.Factory(
        CostumerServiceRepository
    )

    register_costumer_service_use_case = providers.Factory(
        RegisterCostumerServiceUseCase, costumer_service_repo = costumer_service_repo
    )

    response_all_costumer_service_use_case = providers.Factory(
        ResponseAllCostumerServiceUseCase, costumer_service_repo = costumer_service_repo
    )

    response_costumer_service_where_month = providers.Factory(
        ResponseCostumerServiceWhereMonth, costumer_service_repo = costumer_service_repo
    )

    response_costumer_service_where_barber_id_and_where_month = providers.Factory(
        ResponseCostumerServiceWhereBarberIdAndMonth, costumer_service_repo = costumer_service_repo
    )

    response_costumer_servie_where_date = providers.Factory(
        ResponseCostumerServiceWhereDate, costumer_service_repo = costumer_service_repo
    )

    response_costumer_servie_where_barber_id_and_date = providers.Factory(
        ResponseCostumerServiceWhereBarberIdAndDate, costumer_service_repo = costumer_service_repo
    )

    upadate_costumer_service_use_case = providers.Factory(
        UpdateCostumerServiceUseCase, costumer_service_repo = costumer_service_repo
    )