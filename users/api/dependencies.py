from dependency_injector import providers, containers

from users.application.use_case import UserLoginUserCase, UserRegisterUseCase, UserUpdatePasswordUseCase
from users.infrasctuture.repository import UserRepository

class UserContainer(containers.DeclarativeContainer):
    user_repo = providers.Factory(UserRepository)

    user_login_user_case = providers.Factory(
        UserLoginUserCase, user_repo=user_repo
    )

    user_register_use_case = providers.Factory(
        UserRegisterUseCase, user_repo=user_repo
    )

    user_update_password_use_case = providers.Factory(
        UserUpdatePasswordUseCase, user_repo=user_repo
    )
