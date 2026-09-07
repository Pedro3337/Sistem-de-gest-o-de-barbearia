from django.db import models

class AppointmentRole(models.TextChoices):
    agendado = 'AGENDADO', 'agendado'
    cancelado = 'CANCELADO', 'cancelado'
    faltou = 'FALTOU', 'faltou'
    concluido = 'CONCLUIDO' , 'concluido'
    