from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.submit_answer.filters import SubmitAnswerFilter
from api.v1.submit_answer.permissions import SubmitAnswerPermission
from api.v1.submit_answer.serializers import SubmitAnswerSerializer
from app.submit_answer.models import SubmitAnswer


@extend_schema_view(
    list=extend_schema(summary="SubmitAnswer 목록 조회"),
    create=extend_schema(summary="SubmitAnswer 등록"),
    retrieve=extend_schema(summary="SubmitAnswer 상세 조회"),
    update=extend_schema(summary="SubmitAnswer 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="SubmitAnswer 삭제"),
)
class SubmitAnswerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = SubmitAnswer.objects.all()
    serializer_class = SubmitAnswerSerializer
    permission_classes = [SubmitAnswerPermission]
    pagination_class = CursorPagination
    filter_class = SubmitAnswerFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
