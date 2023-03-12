from django.contrib import admin

from app.submit_answer.models import SubmitAnswer


@admin.register(SubmitAnswer)
class SubmitAnswerAdmin(admin.ModelAdmin):
    pass
