from app.explantaion.models import Explantaion
from django.contrib import admin


@admin.register(Explantaion)
class ExplantaionAdmin(admin.ModelAdmin):
    pass
