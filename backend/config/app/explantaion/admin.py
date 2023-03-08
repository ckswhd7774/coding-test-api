from django.contrib import admin

from app.explantaion.models import Explantaion


@admin.register(Explantaion)
class ExplantaionAdmin(admin.ModelAdmin):
    pass
