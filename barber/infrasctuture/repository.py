from barber.domain.entities import BarberEntity
from barber.domain.repositories import IBarberRepository
from barber.infrasctuture.models import Barber
from users.infrasctuture.models import User

class BarberRepositroy(IBarberRepository):
    def save(self, entity: BarberEntity) -> BarberEntity:

        user = User.objects.get(id=entity.user)

        Barber.objects.update_or_create(
            id=entity.id,
            defaults={
                'user': user,
                'phone':entity.phone,
                'commission': entity.commission
            }
        )

        return entity
