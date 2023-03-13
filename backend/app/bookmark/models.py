from django.db import models

from app.common.models import BaseModel


class Bookmark(BaseModel):
    question = models.ForeignKey("question.Question", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "bookmark"
        verbose_name = "북마크"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
