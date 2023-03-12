from django.db import models

from app.common.models import BaseModel


class Explanation(BaseModel):
    class Meta:
        db_table = "explanation"
        verbose_name = "설명"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
