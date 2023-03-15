from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.mock_test_paper.filters import MockTestPaperFilter
from api.v1.mock_test_paper.permissions import MockTestPaperPermission
from api.v1.mock_test_paper.serializers import MockTestPaperSerializer
from app.mock_test_paper.models import MockTestPaper


@extend_schema_view(
    list=extend_schema(summary="MockTestPaper 목록 조회"),
    create=extend_schema(summary="MockTestPaper 등록"),
    retrieve=extend_schema(summary="MockTestPaper 상세 조회"),
    update=extend_schema(summary="MockTestPaper 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="MockTestPaper 삭제"),
)
class MockTestPaperViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = MockTestPaper.objects.all()
    serializer_class = MockTestPaperSerializer
    permission_classes = [MockTestPaperPermission]
    pagination_class = CursorPagination
    filter_class = MockTestPaperFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
