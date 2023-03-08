from django.db import models

from app.common.models import BaseModel


class Question(BaseModel):
    class Meta:
        db_table = "question"
        verbose_name = "Question"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
