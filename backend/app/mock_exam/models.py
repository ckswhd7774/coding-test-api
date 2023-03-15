from django.db import models
from django.utils import timezone

from app.common.models import BaseModel


class MockExam(BaseModel):
    question = models.ForeignKey("question.Question", on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="점수")
    start_time = models.DateTimeField(verbose_name="시작 시간", default=timezone.now)
    end_time = models.DateTimeField(verbose_name="종료 시간", default=timezone.now)

    class Meta:
        db_table = "mock_exam"
        verbose_name = "모의고사 문제"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
