from django.db import models

from app.common.models import BaseModel


class SubmitMock(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    exam = models.ForeignKey("mock_exam.MockExam", on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now_add=True)
    answers = models.JSONField(default=dict)

    class Meta:
        db_table = "submit_mock"
        verbose_name = "모의고사 제출 답"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
