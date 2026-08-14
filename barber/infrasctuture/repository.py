from turtle import mode
from typing import List
from uuid import UUID

from django.utils.timezone import activate

from barber.domain.entities import BarberEntity
from barber.domain.repositories import IBarberRepository
from barber.infrasctuture.models import Barber
from users.infrasctuture.models import User

class BarberRepositroy(IBarberRepository):
    def save(self, entity: BarberEntity) -> BarberEntity:

        user = User.objects.get(id=entity.user.id)

        Barber.objects.update_or_create(
            id=entity.id,
            defaults={
                'user': user,
                'phone':entity.phone,
                'commission': entity.commission,
                'activate': entity.activate
            }
        )

        return entity

    def find_by_id(self, id: UUID):
        try:
            return self._to_model(Barber.objects.get(id=id))
        except Barber.DoesNotExist:
            return None

    def list_all_barber(self) -> List[BarberEntity]:
        return [self._to_model(barber) for barber in Barber.objects.all()]

    def _to_model(self, model: Barber) -> BarberEntity:
        return BarberEntity(
            id=model.id,
            user=model.user,
            phone=model.phone,
            commission=model.commission,
            activate=model.activate,
        )
