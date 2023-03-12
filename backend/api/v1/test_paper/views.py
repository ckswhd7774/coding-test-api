from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.test_paper.filters import TestPaperFilter
from api.v1.test_paper.permissions import TestPaperPermission
from api.v1.test_paper.serializers import TestPaperSerializer
from app.test_paper.models import TestPaper


@extend_schema_view(
    list=extend_schema(summary="TestPaper 목록 조회"),
    create=extend_schema(summary="TestPaper 등록"),
    retrieve=extend_schema(summary="TestPaper 상세 조회"),
    update=extend_schema(summary="TestPaper 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="TestPaper 삭제"),
)
class TestPaperViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = TestPaper.objects.all()
    serializer_class = TestPaperSerializer
    permission_classes = [TestPaperPermission]
    pagination_class = CursorPagination
    filter_class = TestPaperFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset