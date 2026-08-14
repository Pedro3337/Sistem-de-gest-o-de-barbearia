from uuid import uuid4

from django.db import models

class Barber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    phone = models.CharField(default=100)
    commission = models.IntegerField(default=0)
    activate = models.BooleanField(default=False)

    class Meta:
        db_table = 'barbers'