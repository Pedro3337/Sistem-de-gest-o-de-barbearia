from uuid import uuid4

from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    date_register = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'clients'