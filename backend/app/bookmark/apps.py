from django.apps import AppConfig


class BookmarkConfig(AppConfig):
    name = "app.bookmark"

    def ready(self):
        import app.bookmark.signals
