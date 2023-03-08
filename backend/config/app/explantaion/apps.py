from django.apps import AppConfig


class ExplantaionConfig(AppConfig):
    name = "app.explantaion"

    def ready(self):
        import app.explantaion.signals
