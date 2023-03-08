from django.apps import AppConfig


class AnswerConfig(AppConfig):
    name = "app.answer"

    def ready(self):
        import app.answer.signals
