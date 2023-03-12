from django.apps import AppConfig


class TestPaperConfig(AppConfig):
    name = "app.test_paper"

    def ready(self):
        import app.test_paper.signals
