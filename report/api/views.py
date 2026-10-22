from datetime import date
from urllib.error import HTTPError
from uuid import UUID

from ninja import Router

from report.api.dependencies import ReportContainer
from report.api.schema import DashboardBarberOut,DashboardOut
from users.domain.role import UserRole
from users.infrasctuture.auth.jwt_auth import JWTAuth

router = Router()
container = ReportContainer()

@router.get('/admin/', auth=JWTAuth(), response=DashboardOut)
def response_report_of_dashboard(request, year: int, month: int):
    current_user = request.auth
    
    if current_user.role != UserRole.admin:
        raise  HTTPError(403, "Você não possui permissão para cadastrar barbeiros.")

    use_case = container.response_report_use_case()

    response = use_case.execute(year, month)

    return DashboardOut.from_domain(response)


@router.get('/barber/', auth=JWTAuth(), response=DashboardBarberOut)
def response_report_of_dashboard_barber(request, id: UUID, date: date, month: int):
    current_user = request.auth
    
    if current_user.role != UserRole.barbeiro:
        raise  HTTPError(403, "Você não possui permissão para cadastrar barbeiros.")

    use_case = container.response_report_barber_use_case()

    response = use_case.execute(id, month, date)

    return DashboardBarberOut.from_domain(response)
