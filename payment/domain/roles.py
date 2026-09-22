from django.db import models

class PaymentRole(models.TextChoices):
    pix = 'PIX','Pix'
    dinheito = 'DINHEIRO','Dinheiro'
    debito = 'DEBITO', 'Débito'
    credito = 'CREDITO', 'Crédito'

class PaymantStatusRole(models.TextChoices):
    pago = 'PAGO','Pago'
    estornado = 'ESTORNADO','Estornado'