from datetime import datetime
from typing import List
from uuid import UUID

from ninja import Router

from appointments.api.dependencies import AppointmentContainer
from appointments.api.schemas import AppointmentIn, AppointmentOut, AppointmentUpdate

from django.db.transaction import atomic

router = Router()
container = AppointmentContainer()

@router.post('/', response=AppointmentOut)
@atomic
def register_appointment(request, data: AppointmentIn):
    dto = data.to_dto()

    use_case = container.register_appointment_use_case()

    appointment = use_case.execute(dto)

    return AppointmentOut.from_domain(appointment)

@router.get('/', response=List[AppointmentOut])
def response_all_appointment(request):
    use_case = container.response_all_appointment()

    appointments_dto = use_case.execute()

    return [
        AppointmentOut.from_domain(appointment)
        for appointment in appointments_dto
    ]

@router.get('/barber/', response=List[AppointmentOut])
def response_appointments_where_barber_id(request, id: UUID):
    use_case = container.response_appointment_where_barber_id()

    appointments_dto = use_case.execute(id)

    return [
        AppointmentOut.from_domain(appointment)
        for appointment in appointments_dto
    ]

@router.get('/client/', response=AppointmentOut)
def response_appointments_where_client_id(request, id: UUID):
    use_case = container.response_appointment_where_client_id()

    response = use_case.execute(id)

    return AppointmentOut.from_domain(response)

@router.get('/barber/date/', response=List[AppointmentOut])
def response_appointments_where_barber_id(request, id: UUID, date: datetime):
    use_case = container.response_appointment_where_barber_id_and_date()

    appointments_dto = use_case.execute(id, date)

    return [
        AppointmentOut.from_domain(appointment)
        for appointment in appointments_dto
    ]

@router.put('/atualizar/{id}/', response=AppointmentOut)
def update_appointment(request,data: AppointmentUpdate, id: UUID):
    dto = data.to_dto()

    use_case = container.update_appointment_use_case()

    appointment = use_case.execute(dto, id)

    return AppointmentOut.from_domain(appointment)




    