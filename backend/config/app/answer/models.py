from django.db import models

from app.common.models import BaseModel


class Answer(BaseModel):
    class Meta:
        db_table = "answer"
        verbose_name = "Answer"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
