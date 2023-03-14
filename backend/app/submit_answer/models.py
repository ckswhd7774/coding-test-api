from django.db import models

from app.common.models import BaseModel


class StatusChoices(models.IntegerChoices):
    in_progress = 1, "채점 중"
    complete = 2, "채점 완료"


class SubmitAnswer(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    question = models.ForeignKey("question.Question", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="내용")
    is_correct = models.BooleanField(verbose_name="정답 유무", default=False)
    score = models.PositiveSmallIntegerField(verbose_name="점수", default=0)
    status = models.PositiveSmallIntegerField(verbose_name="상태", choices=StatusChoices.choices)

    class Meta:
        db_table = "submit_answer"
        verbose_name = "제출 답"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
