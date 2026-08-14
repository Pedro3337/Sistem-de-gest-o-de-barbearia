from dependency_injector import containers,providers

from barber.application.use_case import AbledBarberUseCase, ResponseAllBarberUseCase
from barber.infrasctuture.repository import BarberRepositroy

class BarberContainer(containers.DeclarativeContainer):
    barber_repo = providers.Factory(BarberRepositroy)

    response_barber_all_use_case = providers.Factory(
        ResponseAllBarberUseCase, barber_repo = barber_repo
    )

    abled_barber_use_case = providers.Factory(
        AbledBarberUseCase, barber_repo = barber_repo
    )
