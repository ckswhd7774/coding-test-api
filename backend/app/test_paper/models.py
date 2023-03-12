from django.db import models

from app.common.models import BaseModel


class TestPaper(BaseModel):
    title = models.CharField(verbose_name="시험지 명", max_length=64)
    text = models.TextField(verbose_name="내용")
    time_limit = models.SmallIntegerField(verbose_name='제한 시간')

    class Meta:
        db_table = "test_paper"
        verbose_name = "모의고사"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]


class QuestionInTestPaper(BaseModel):
    test_paper = models.ForeignKey("test_paper.TestPaper", on_delete=models.CASCADE)
    question = models.ForeignKey("question.Question", on_delete=models.CASCADE)  # bulk_create

    class Meta:
        db_table = "question_test_paper"
        verbose_name = "모의고사 문제"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
