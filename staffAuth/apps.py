from django.apps import AppConfig


class StaffAuthConfig(AppConfig):
    name = 'staffAuth'

    def ready(self):
        import staffAuth.signals
