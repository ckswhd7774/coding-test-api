from django.contrib import admin

from app.question.models import Question, QuestionCategory


@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
