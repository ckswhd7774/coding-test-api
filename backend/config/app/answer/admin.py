from app.answer.models import Answer
from django.contrib import admin


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
