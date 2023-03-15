from django.contrib import admin

from app.mock_exam.models import MockExam


@admin.register(MockExam)
class MockExamAdmin(admin.ModelAdmin):
    pass
