from django.apps import AppConfig


class PaypalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paypal_app'

    def ready(self):
        import paypal_app.signals