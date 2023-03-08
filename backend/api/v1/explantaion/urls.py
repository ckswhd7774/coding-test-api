from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.explantaion.views import ExplantaionViewSet

router = DefaultRouter()
router.register("explantaion", ExplantaionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
