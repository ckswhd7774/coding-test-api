from django.contrib import admin

from app.test_paper.models import QuestionInTestPaper, TestPaper


@admin.register(TestPaper)
class TestPaperAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionInTestPaper)
class QuestionInTestPaperAdmin(admin.ModelAdmin):
    pass
