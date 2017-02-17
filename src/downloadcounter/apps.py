from django.apps import AppConfig


class CounterAppConfig(AppConfig):
    name = 'downloadcounter'

    def ready(self):
        import downloadcounter.signals  # NOQA
