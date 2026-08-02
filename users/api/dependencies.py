from dependency_injector import providers, containers

from barber.infrasctuture.repository import BarberRepositroy
from clients.infrasctuture.repository import ClienteRepository
from users.application.use_case import RegisterBarberUseCase, UserLoginUserCase, UserRegisterUseCase, UserUpdatePasswordUseCase
from users.infrasctuture.repository import UserRepository

class UserContainer(containers.DeclarativeContainer):
    user_repo = providers.Factory(UserRepository)
    client_repo = providers.Factory(ClienteRepository)
    barber_repo = providers.Factory(BarberRepositroy)

    user_login_user_case = providers.Factory(
        UserLoginUserCase, user_repo=user_repo
    )

    user_register_use_case = providers.Factory(
        UserRegisterUseCase, user_repo=user_repo, client_repo=client_repo
    )

    user_update_password_use_case = providers.Factory(
        UserUpdatePasswordUseCase, user_repo=user_repo
    )

    barber_register_use_case = providers.Factory(
        RegisterBarberUseCase, user_repo=user_repo, barber_repo = barber_repo
    )
