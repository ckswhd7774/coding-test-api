from django.contrib import admin

from app.question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
