from uuid import uuid4

from django.db import models

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    value = models.FloatField(default=0)
    activate = models.BooleanField(default=True)

    class Meta:
        db_table = 'services'
