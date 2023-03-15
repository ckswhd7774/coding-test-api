from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.submit_mock.filters import SubmitMockFilter
from api.v1.submit_mock.permissions import SubmitMockPermission
from api.v1.submit_mock.serializers import SubmitMockSerializer
from app.submit_mock.models import SubmitMock


@extend_schema_view(
    list=extend_schema(summary="SubmitMock 목록 조회"),
    create=extend_schema(summary="SubmitMock 등록"),
    retrieve=extend_schema(summary="SubmitMock 상세 조회"),
    update=extend_schema(summary="SubmitMock 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="SubmitMock 삭제"),
)
class SubmitMockViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = SubmitMock.objects.all()
    serializer_class = SubmitMockSerializer
    permission_classes = [SubmitMockPermission]
    pagination_class = CursorPagination
    filter_class = SubmitMockFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
