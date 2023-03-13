from django.db.models import Exists, OuterRef, F, Avg
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.common.pagination import CursorPagination
from api.v1.question.filters import QuestionFilter
from api.v1.question.permissions import QuestionPermission
from api.v1.question.serializers import QuestionSerializer
from app.question.models import Question
from app.submit_answer.models import SubmitAnswer


@extend_schema_view(
    list=extend_schema(summary="Question 목록 조회"),
    create=extend_schema(summary="Question 등록"),
    retrieve=extend_schema(summary="Question 상세 조회"),
    update=extend_schema(summary="Question 수정"),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(summary="Question 삭제"),
)
class QuestionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [QuestionPermission]
    pagination_class = CursorPagination
    filter_class = QuestionFilter
    lookup_url_kwarg = "question_id"

    def get_queryset(self):
        queryset = (
            Question.objects.select_related("category", "explanation")
            .annotate(
                is_submitted=Exists(
                    SubmitAnswer.objects.filter(user_id=self.request.user.id, question_id=OuterRef("id"))
                ),
                score_avg=Avg("submitanswer__score"),
            )
            .prefetch_related("submitanswer_set")
            .order_by("level", "submit_count", "-created_at", "score_avg")
        )
        return queryset
