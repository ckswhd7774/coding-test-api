from django.apps import AppConfig


class QuestionConfig(AppConfig):
    name = "app.question"

    def ready(self):
        import app.question.signals
