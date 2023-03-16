from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.answer.filters import AnswerFilter
from api.v1.answer.permissions import AnswerPermission
from api.v1.answer.serializers import AnswerSerializer
from app.answer.models import Answer
from config.cache import cache_get_queryset


@extend_schema_view(
    list=extend_schema(summary="Answer 목록 조회"),
    create=extend_schema(summary="Answer 등록"),
    retrieve=extend_schema(summary="Answer 상세 조회"),
    update=extend_schema(summary="Answer 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="Answer 삭제"),
)
class AnswerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AnswerPermission]
    pagination_class = CursorPagination
    filter_class = AnswerFilter
    lookup_url_kwarg = "answer_id"

    @cache_get_queryset("answer")
    def get_queryset(self):
        queryset = Answer.objects.select_related("question", "question__explanation").filter(
            question_id=self.kwargs["question_id"]
        )
        return queryset
