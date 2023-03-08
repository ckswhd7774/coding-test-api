from django.contrib import admin

from app.answer.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
