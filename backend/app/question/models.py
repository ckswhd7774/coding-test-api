from django.db import models

from app.common.models import BaseModel


class QuestionTypeChoices(models.IntegerChoices):
    stack_q = 1, "스택&큐"
    e_s = 2, "완전탐색"
    dp = 3, "DP"
    bfs = 4, "BFS"


class QuestionCategory(BaseModel):
    name = models.CharField(verbose_name="유형 이름", max_length=32)

    class Meta:
        db_table = "question_category"
        verbose_name = "문제 유형"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]


class Question(BaseModel):
    category = models.ForeignKey("question.QuestionCategory", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목", max_length=64)
    text = models.TextField(verbose_name="내용")
    restrictions = models.TextField(verbose_name="제한 사항", null=True, blank=True)
    level = models.PositiveSmallIntegerField(verbose_name="난이도")
    score = models.PositiveSmallIntegerField(verbose_name="점수")
    submit_count = models.IntegerField(verbose_name="응시 횟수", default=0)

    class Meta:
        db_table = "question"
        verbose_name = "문제"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
