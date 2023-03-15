from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.mock_exam.filters import MockExamFilter
from api.v1.mock_exam.permissions import MockExamPermission
from api.v1.mock_exam.serializers import MockExamSerializer
from app.mock_exam.models import MockExam


@extend_schema_view(
    list=extend_schema(summary="MockExam 목록 조회"),
    create=extend_schema(summary="MockExam 등록"),
    retrieve=extend_schema(summary="MockExam 상세 조회"),
    update=extend_schema(summary="MockExam 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="MockExam 삭제"),
)
class MockExamViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = MockExam.objects.all()
    serializer_class = MockExamSerializer
    permission_classes = [MockExamPermission]
    pagination_class = CursorPagination
    filter_class = MockExamFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
