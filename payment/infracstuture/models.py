from uuid import uuid4

from django.db import models

from payment.domain.roles import PaymantStatusRole, PaymentRole


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    costumer_service_id = models.ForeignKey(
        'costumerservice.CostumerService'
        ,on_delete=models.CASCADE
    )
    payment_method = models.CharField(max_length=20, choices=PaymentRole, default=PaymentRole.pix)
    value = models.FloatField(default=0)
    date_payment = models.DateField()
    status = models.CharField(max_length=20, choices=PaymantStatusRole, default=PaymantStatusRole.pago)
