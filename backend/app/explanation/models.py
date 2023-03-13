from django.db import models

from app.common.models import BaseModel


class Explanation(BaseModel):
    question = models.OneToOneField("question.Question", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="내용")

    class Meta:
        db_table = "explanation"
        verbose_name = "해설"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
