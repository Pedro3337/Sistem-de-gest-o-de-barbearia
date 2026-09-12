from email.policy import default
from random import choices
from uuid import uuid4

from django.db import models
from django.db.models.fields import TextField
from django.forms.fields import CharField

from appointments.application.role import AppointmentRole

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
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
    time = models.TimeField()
    status = CharField(max_length=30, choices=AppointmentRole, default=AppointmentRole.agendado)
    observation = TextField()
    