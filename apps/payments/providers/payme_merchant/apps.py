from django.apps import AppConfig


class PaymeMerchantConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.payments.providers.payme_merchant"
