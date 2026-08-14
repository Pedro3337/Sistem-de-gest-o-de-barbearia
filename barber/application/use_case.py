from typing import List
from uuid import UUID

from barber.application.dtos import BarberOutDTO, BarberUpdateDTO
from barber.domain.repositories import IBarberRepository

class ResponseAllBarberUseCase:
    def __init__(self, barber_repo: IBarberRepository):
        self.barber_repo = barber_repo

    def execute(self) -> List[BarberOutDTO]:
        barbers = self.barber_repo.list_all_barber()

        return [BarberOutDTO.from_domain(barber) for barber in barbers]

class AbledBarberUseCase:
    def __init__(self, barber_repo: IBarberRepository):
        self.barber_repo = barber_repo

    def execute(self, dto: BarberUpdateDTO, id: UUID) -> BarberOutDTO:
        barber = self.barber_repo.find_by_id(id)

        if not barber:
            raise Exception('Barber not found')

        if dto.phone:
            barber.change_phone(dto.phone)

        if dto.commission:
            barber.change_comission(dto.commission)

        barber.change_activate(dto.activate)

        return BarberOutDTO.from_domain(self.barber_repo.save(barber))

class ViewAgendaUseCase:
    def __init__(self, barber_repo: IBarberRepository):
        self.barber_repo = barber_repo