from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.mock_test_paper.views import MockTestPaperViewSet

router = DefaultRouter()
router.register("mock_test_paper", MockTestPaperViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
