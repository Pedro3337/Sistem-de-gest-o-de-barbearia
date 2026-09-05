from typing import List
from uuid import UUID

from ninja import Router

from service.api.dependencies import ServiceContainer
from service.api.schemas import ServiceIn, ServiceOut, ServiceUpdate
from service.infrasctuture.models import Service

router = Router()
container = ServiceContainer()

@router.post('/', response=ServiceOut)
def register_service(request, data: ServiceIn):
    dto = data.to_dto()

    use_case = container.register_service_use_case()

    response = use_case.execute(dto)

    return ServiceOut.from_domain(response)

@router.put('/', response=ServiceOut)
def update_service(request, id: UUID, data: ServiceUpdate):
    dto = data.to_dto()

    use_case = container.update_service_use_case()

    response = use_case.execute(id, dto)

    return ServiceOut.from_domain(response)

@router.get('/', response=List[ServiceOut])
def response_service_all(request):
    use_case = container.response_all_services_use_case()

    servicesDto = use_case.execute()

    return [ServiceOut.from_domain(service) for service in servicesDto]

    