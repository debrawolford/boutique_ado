from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def reasy(self):
        import.checkout.signals
