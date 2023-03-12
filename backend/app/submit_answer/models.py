from django.db import models

from app.common.models import BaseModel


class SubmitAnswer(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    question = models.ForeignKey("question.Question", on_delete=models.CASCADE)
    is_correct = models.BooleanField(verbose_name="정답 유무")

    class Meta:
        db_table = "submit_answer"
        verbose_name = "제출 답"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
