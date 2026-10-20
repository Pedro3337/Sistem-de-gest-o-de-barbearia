from typing import List
from uuid import UUID

from ninja import Router

from payment.api.dependencies import PaymentContainer
from payment.api.schemas import PaymentIn, PaymentOut, PaymentUpdate

router = Router()
container = PaymentContainer()

@router.post('/', response=PaymentOut)
def register_payment(request, data: PaymentIn):
    dto = data.to_dto()

    use_case = container.register_payment_use_case()

    response = use_case.execute(dto)

    return PaymentOut.from_domain(response)

@router.get('/', response=List[PaymentOut])
def list_all_payments(request):
    use_case = container.response_list_all_use_case()

    payments = use_case.execute()

    return [PaymentOut.from_domain(payment) for payment in payments]

@router.get('/month/', response=List[PaymentOut])
def list_payment_where_month(request, month: int):
    use_case = container.response_list_payment_where_month_use_case()

    payments = use_case.execute(month)

    return [PaymentOut.from_domain(payment) for payment in payments]

@router.get('/year/', response=List[PaymentOut])
def list_payment_where_year(request, year: int):
    use_case = container.response_list_payment_where_year_use_case()

    payments = use_case.execute(year)

    return [PaymentOut.from_domain(payment) for payment in payments]

@router.put('/', response=PaymentOut)
def update_payment(request, data: PaymentUpdate, id: UUID):
    dto = data.to_dto()

    use_case = container.update_payment_use_case()

    response = use_case.execute(dto, id)

    return PaymentOut.from_domain(response)