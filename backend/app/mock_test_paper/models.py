from django.db import models

from app.common.models import BaseModel


class MockTestPaper(BaseModel):
    question = models.ManyToManyField("question.Question", blank=True)
    title = models.CharField(verbose_name="시험지 명", max_length=64)

    class Meta:
        db_table = "mock_test_paper"
        verbose_name = "모의고사 문제지"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
