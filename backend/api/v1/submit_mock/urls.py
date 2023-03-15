from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.submit_mock.views import SubmitMockViewSet

router = DefaultRouter()
router.register("submit_mock", SubmitMockViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
