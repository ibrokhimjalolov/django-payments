from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class BaseOrder(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name="orders")

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")
        abstract = True


class Order(BaseOrder):
    """
    Order model
    """

    class Meta(BaseOrder.Meta):
        swappable = "PAYMENT_ORDER_MODEL"
