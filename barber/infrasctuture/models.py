from uuid import uuid4

from django.db import models

class Barber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    phone = models.CharField(default=100)
    commission = models.DecimalField(max_digits=5, decimal_places=2)
    activate = models.BooleanField(default=True)

    class Meta:
        db_table = 'barbers'