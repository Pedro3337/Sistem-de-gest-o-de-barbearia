from datetime import date
from typing import List
from uuid import UUID

from ninja import Router

from costumerservice.api.dependencies import CostumerServiceContainer
from costumerservice.api.schemas import ConstumerServiceUpdate, CostumerServiceIn, CostumerServiceOut

router = Router()
container = CostumerServiceContainer()

@router.post('/', response=CostumerServiceOut)
def register_costumer_service(request, data: CostumerServiceIn):
    dto = data.to_dto()

    use_case = container.register_costumer_service_use_case()

    response = use_case.execute(dto)

    return CostumerServiceOut.from_domain(response)

@router.get('/costumers/', response=List[CostumerServiceOut])
def response_all_costumer_service(request):
    use_case = container.response_all_costumer_service_use_case()

    costumer_services = use_case.execute()

    return [CostumerServiceOut.from_domain(costumer_service) for costumer_service in costumer_services]

@router.get('/costumers/month/', response=List[CostumerServiceOut])
def response_costumer_service_where_month(request, month: int):
    use_case = container.response_costumer_service_where_month()

    costumer_services = use_case.execute(month)

    return [CostumerServiceOut.from_domain(costumer_service) for costumer_service in costumer_services]

@router.get('/costumers/month/barber/', response=List[CostumerServiceOut])
def response_costumer_service_where_month(request,barber: UUID, month: int):
    use_case = container.response_costumer_service_where_barber_id_and_where_month()

    costumer_services = use_case.execute(barber, month)

    return [CostumerServiceOut.from_domain(costumer_service) for costumer_service in costumer_services]

@router.get('/costumers/date/', response=List[CostumerServiceOut])
def response_costumer_service_where_date(request, date: date):
    use_case = container.response_costumer_servie_where_date()

    costumer_services = use_case.execute(date)

    return [CostumerServiceOut.from_domain(costumer_service) for costumer_service in costumer_services]

@router.get('/costumers/date/barber/', response=List[CostumerServiceOut])
def response_costumer_service_where_date(request, barber: UUID, date: date):
    use_case = container.response_costumer_servie_where_barber_id_and_date()

    costumer_services = use_case.execute(barber, date)

    return [CostumerServiceOut.from_domain(costumer_service) for costumer_service in costumer_services]

@router.put('/', response=CostumerServiceOut)
def update_costumer_service(request, data: ConstumerServiceUpdate, id: UUID):
    dto = data.to_dto()

    use_case = container.upadate_costumer_service_use_case()

    response = use_case.execute(dto, id)

    return CostumerServiceOut.from_domain(response)

