from calendar import month
from datetime import date
import re
from typing import List
from uuid import UUID

import appointments
from appointments.infracstuture.models import Appointment
from clients.infrasctuture.models import Client

from barber.infrasctuture.models import Barber
from costumerservice.domain.entities import CostumerServiceEntity
from costumerservice.domain.repositories import ICostumerServiceRepository
from costumerservice.infracstuture.models import CostumerService
from service.infrasctuture.models import Service


class CostumerServiceRepository(ICostumerServiceRepository):
    def save(self, entity: CostumerServiceEntity) -> CostumerServiceEntity:
        client = Client.objects.get(id=entity.client)
        barber = Barber.objects.get(id=entity.barber)
        service = Service.objects.get(id=entity.service)
        appointment = Appointment.objects.get(id=entity.appointment)
        CostumerService.objects.update_or_create(
            id=entity.id,
            defaults={
                'appointment': appointment,
                'client': client,
                'barber': barber,
                'service': service,
                'date': entity.date_a,
                'month': entity.month,
                'deduct': entity.deduct,
                'total_value': entity.total_value,
                'end_value': entity.end_value,
                'observation': entity.observation
            }
        )

        return entity

    def find_by_id(self, id: UUID) -> CostumerServiceEntity:
        try:
            return self._to_model(CostumerService.objects.get(id=id))
        except CostumerService.DoesNotExist:
            return None

    def response_all_costumer_service(self, ) -> List[CostumerServiceEntity]:
        try:
            return [self._to_model(costumer_service) for costumer_service in CostumerService.objects.all()]
        except CostumerService.DoesNotExist:
            return None

    def response_costumer_service_where_month(self, month: int) -> List[CostumerServiceEntity]:
        try:
            return [self._to_model(costumer_service) for costumer_service in CostumerService.objects.filter(month=month)]
        except CostumerService.DoesNotExist:
            return None

    def response_costumer_service_where_barber_id_and_month(self, barber: UUID, month: int) -> List[CostumerServiceEntity]:
        try:
            return [self._to_model(costumer_service) for costumer_service in CostumerService.objects.filter(barber=barber, month=month)]
        except CostumerService.DoesNotExist:
            return None

    def response_costumer_service_where_date(self, date: date) -> List[CostumerServiceEntity]:
        try:
            return [self._to_model(costumer_service) for costumer_service in CostumerService.objects.filter(date=date)]
        except CostumerService.DoesNotExist:
            return None

    def response_costumer_service_where_barber_id_and_date(self, barber: UUID, date: date) -> List[CostumerServiceEntity]:
        try:
            return [self._to_model(costumer_service) for costumer_service in CostumerService.objects.filter(barber=barber, month=month)]
        except CostumerService.DoesNotExist:
            return None

    def _to_model(self, model=CostumerServiceEntity) -> CostumerServiceEntity:
        return CostumerServiceEntity(
            id=model.id,
            appointment=model.appointment.id,
            client=model.client.id,
            barber=model.barber.id,
            service=model.service.id,
            date_a=model.date,
            month=model.month,
            deduct=model.deduct,
            total_value=model.total_value,
            end_value=model.end_value,
            observation=model.observation,
        )
