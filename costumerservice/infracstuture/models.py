from pyexpat import model
from turtle import mode
from uuid import uuid4

from django.db import models

class CostumerService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    appointment = models.ForeignKey(
        'appointments.Appointment',
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        'clients.Client', on_delete=models.CASCADE
    )
    barber = models.ForeignKey(
        'barber.Barber', on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        'service.Service', on_delete=models.CASCADE
    )
    date = models.DateField()
    month = models.IntegerField()
    time = models.TimeField()
    observation = models.TextField()

    class Meta:
        db_table = 'ConstumerService'
