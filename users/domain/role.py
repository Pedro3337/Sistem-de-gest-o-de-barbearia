from django.db import models

class UserRole(models.TextChoices):
    cliente = 'CLIENTE','cliente'
    barbeiro = 'BARBEIRO','barbeiro'