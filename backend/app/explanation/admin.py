from django.contrib import admin

from app.explanation.models import Explanation


@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
    pass
