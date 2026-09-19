from datetime import date
from typing import List
from uuid import UUID

from ninja import Router
from django.db.transaction import atomic

import appointments
from appointments.api.dependencies import AppointmentContainer
from appointments.api.schemas import AppointmentIn, AppointmentOut, AppointmentUpdate

router = Router()
container = AppointmentContainer()

@router.post('/', response=AppointmentOut)
@atomic
def register_appointment(request, data: AppointmentIn):
    dto = data.to_dto()

    use_case = container.register_appointment_repo()

    response = use_case.execute(dto)

    return AppointmentOut.from_domain(response)

@router.get('/appointments/', response=List[AppointmentOut])
def response_all_appointments(request):
    use_case = container.response_all_appointments_use_case()

    appointments = use_case.execute()

    return [AppointmentOut.from_domain(appointment) for appointment in appointments]

@router.get('/appointment/client/', response=List[AppointmentOut])
def response_client_appointments(request, id: UUID):
    use_case = container.response_appointment_where_client_id()

    appointments = use_case.execute(id)

    return [AppointmentOut.from_domain(appointment) for appointment in appointments]

@router.get('/appointments/barber/', response=List[AppointmentOut])
def response_barber_appointments(request, id: UUID):
    use_case = container.response_list_appointment_where_barber_id_use_case()

    appointments = use_case.execute(id)

    return [AppointmentOut.from_domain(appointment) for appointment in appointments]

@router.get('/appointments/barber/date', response=List[AppointmentOut])
def response_barber_appointments_where_id_and_date(request, id: UUID, date: date):
    use_case = container.response_list_appointment_where_barber_id_and_date_use_case()

    appointments = use_case.execute(id, date)

    return [AppointmentOut.from_domain(appointment) for appointment in appointments]

@router.put('/', response=AppointmentOut)
def update_appointment(request, data: AppointmentUpdate, id: UUID):
    dto = data.to_dto()

    use_case = container.update_apointment_use_case()

    response = use_case.execute(dto, id)

    return AppointmentOut.from_domain(response)