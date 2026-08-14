from typing import List
from urllib.error import HTTPError
from uuid import UUID

from ninja import Router

from barber.api.dependencies import BarberContainer
from barber.api.schema import BarberOut, BarberUpdate
from users.domain.role import UserRole

router = Router()
container = BarberContainer()

@router.get('/', response=List[BarberOut])
def list_barber_all(request):
    use_case = container.response_barber_all_use_case()

    barbers = use_case.execute()

    return [BarberOut.from_domain(barber) for barber in barbers]

@router.put('/{id}/',response=BarberOut)
def update_barber(request, data: BarberUpdate, id: UUID):
    dto = data.to_dto()

    use_case = container.abled_barber_use_case()

    return BarberOut.from_domain(use_case.execute(dto, id))