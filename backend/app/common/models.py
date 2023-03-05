from django.db import models
from django.utils import timezone


class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(verbose_name="생성일시", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True


BaseModel = BaseModelMixin
