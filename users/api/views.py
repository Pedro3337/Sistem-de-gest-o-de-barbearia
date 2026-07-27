from uuid import UUID

from ninja import Router

from users.api.LoginSchema import LoginResponse
from users.api.dependencies import UserContainer
from users.api.schemas import UserIn, UserOut, UserRegisterIn
from users.infrasctuture.models import User

router = Router()
container = UserContainer()

@router.post('/{password}', response=LoginResponse)
def login_user(request, data: UserIn, password: str):

    dto = data.to_dto()

    use_case = container.user_login_user_case()

    response = use_case.execute(dto, password)

    return LoginResponse.from_domain(response)

@router.post('/register/', response=UserOut)
def register_use(request, data: UserRegisterIn):
    dto = data.to_dto()

    use_case = container.user_register_use_case()

    user = use_case.execute(dto)

    return UserOut.from_domain(user)


@router.put('/{id}/{new_password}', response=UserOut)
def update_password(request, id: UUID, new_password: str):
    user_case = container.user_update_password_use_case()

    response = user_case.execute(id, new_password)

    return UserOut.from_domain(response)

