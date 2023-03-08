from django.db import models

from app.common.models import BaseModel


class Explantaion(BaseModel):
    class Meta:
        db_table = "explantaion"
        verbose_name = "Explantaion"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]
