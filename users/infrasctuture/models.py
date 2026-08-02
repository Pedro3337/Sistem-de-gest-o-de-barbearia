from uuid import uuid4

from django.db import models

from users.domain.role import UserRole

class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=UserRole)
    activate = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name