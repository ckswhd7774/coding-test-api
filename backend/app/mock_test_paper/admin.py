from django.contrib import admin

from app.mock_test_paper.models import MockTestPaper


@admin.register(MockTestPaper)
class MockTestPaperAdmin(admin.ModelAdmin):
    pass
