from uuid import uuid4

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'