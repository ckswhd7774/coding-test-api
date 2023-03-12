from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.explanation.views import ExplanationViewSet

router = DefaultRouter()
router.register("explanation", ExplanationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
