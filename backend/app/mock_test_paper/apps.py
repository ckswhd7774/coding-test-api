from django.apps import AppConfig


class MockTestPaperConfig(AppConfig):
    name = "app.mock_test_paper"

    def ready(self):
        import app.mock_test_paper.signals
