from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.question.views import QuestionViewSet

router = DefaultRouter()
router.register("question", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
