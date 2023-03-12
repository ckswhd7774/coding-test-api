from django.apps import AppConfig


class SubmitAnswerConfig(AppConfig):
    name = "app.submit_answer"

    def ready(self):
        import app.submit_answer.signals
