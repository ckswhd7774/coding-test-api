from django.apps import AppConfig


class SubmitMockConfig(AppConfig):
    name = "app.submit_mock"

    def ready(self):
        import app.submit_mock.signals
