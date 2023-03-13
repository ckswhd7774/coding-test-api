from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.bookmark.views import BookmarkViewSet

router = DefaultRouter()
router.register("bookmark", BookmarkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
