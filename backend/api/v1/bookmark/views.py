from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.bookmark.filters import BookmarkFilter
from api.v1.bookmark.permissions import BookmarkPermission
from api.v1.bookmark.serializers import BookmarkSerializer
from app.bookmark.models import Bookmark


@extend_schema_view(
    list=extend_schema(summary="Bookmark 목록 조회"),
    create=extend_schema(summary="Bookmark 등록"),
    retrieve=extend_schema(summary="Bookmark 상세 조회"),
    update=extend_schema(summary="Bookmark 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="Bookmark 삭제"),
)
class BookmarkViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [BookmarkPermission]
    pagination_class = CursorPagination
    filter_class = BookmarkFilter

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
