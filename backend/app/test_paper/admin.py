from django.contrib import admin

from app.test_paper.models import TestPaper, QuestionInTestPaper


@admin.register(TestPaper)
class TestPaperAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionInTestPaper)
class QuestionInTestPaperAdmin(admin.ModelAdmin):
    pass
