from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.mock_exam.views import MockExamViewSet

router = DefaultRouter()
router.register("mock_exam", MockExamViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
