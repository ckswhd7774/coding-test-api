from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import Group
from django.urls import path
from django.utils.safestring import mark_safe

urlpatterns = [
    path('', admin.site.urls),
]


