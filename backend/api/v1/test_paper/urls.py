from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.test_paper.views import TestPaperViewSet

router = DefaultRouter()
router.register("test_paper", TestPaperViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
