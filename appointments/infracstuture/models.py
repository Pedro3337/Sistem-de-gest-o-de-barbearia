from email.policy import default
from uuid import uuid4

from django.db import models

from appointments.domain.role import AppointmentRole

class Appointments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    client_id = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE
    )

    barber_id = models.ForeignKey(
        'barber.Barber',
        on_delete=models.CASCADE
    )

    service_id = models.ForeignKey(
        'service.Service',
        on_delete=models.CASCADE
    )

    date_time = models.DateTimeField()
    status = models.CharField(
        max_length=100, choices=AppointmentRole, default=AppointmentRole.agendado
    )

    observation = models.TextField()