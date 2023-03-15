from django.contrib import admin

from app.submit_mock.models import SubmitMock


@admin.register(SubmitMock)
class SubmitMockAdmin(admin.ModelAdmin):
    pass
