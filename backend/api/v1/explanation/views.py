from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.explanation.filters import ExplanationFilter
from api.v1.explanation.permissions import ExplantaionPermission
from api.v1.explanation.serializers import ExplanationSerializer
from app.explanation.models import Explanation
from config.cache import cache_get_queryset


@extend_schema_view(
    list=extend_schema(summary="Explantaion 목록 조회"),
    create=extend_schema(summary="Explantaion 등록"),
    retrieve=extend_schema(summary="Explantaion 상세 조회"),
    update=extend_schema(summary="Explantaion 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="Explantaion 삭제"),
)
class ExplanationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Explanation.objects.all()
    serializer_class = ExplanationSerializer
    permission_classes = [ExplantaionPermission]
    pagination_class = CursorPagination
    filter_class = ExplanationFilter
    lookup_url_kwarg = "explanation_id"

    @cache_get_queryset("explanation")
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
