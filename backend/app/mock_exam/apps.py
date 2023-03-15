from django.apps import AppConfig


class MockExamConfig(AppConfig):
    name = "app.mock_exam"

    def ready(self):
        import app.mock_exam.signals
