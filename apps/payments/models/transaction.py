from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


ORDER_MODEL = getattr(settings, "PAYMENT_ORDER_MODEL", "payments.Order")


class BaseTransaction(models.Model):
    """
    Transaction model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order = models.ForeignKey(ORDER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    request_id = models.CharField(max_length=255, null=True)
    transaction_id = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")
        abstract = True


class Transaction(BaseTransaction):
    """
    Transaction model
    """

    class Meta(BaseTransaction.Meta):
        swappable = "PAYMENT_TRANSACTION_MODEL"
