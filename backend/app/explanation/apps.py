from django.apps import AppConfig


class ExplanationConfig(AppConfig):
    name = "app.explanation"

    def ready(self):
        import app.explanation.signals
