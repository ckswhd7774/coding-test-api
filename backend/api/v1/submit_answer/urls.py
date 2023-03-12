from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.submit_answer.views import SubmitAnswerViewSet

router = DefaultRouter()
router.register("submit_answer", SubmitAnswerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
