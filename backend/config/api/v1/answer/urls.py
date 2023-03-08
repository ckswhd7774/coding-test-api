from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.answer.views import AnswerViewSet

router = DefaultRouter()
router.register("answer", AnswerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
