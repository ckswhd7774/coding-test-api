from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models

from app.common.models import BaseModel, BaseModelMixin


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.model.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(BaseModelMixin, AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(verbose_name="이름", max_length=6)
    email = models.EmailField(verbose_name="이메일", null=True, blank=True, unique=True)
    phone = models.CharField(verbose_name="휴대폰", max_length=11, unique=True, null=True, blank=True)
    birth_date = models.DateField(verbose_name="생일", auto_now=False, auto_now_add=False, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # 빈값 유지
    VERIFY_FIELDS = ["email"]  # 회원가입 시 검증 받을 필드 (email, phone)
    REGISTER_FIELDS = ["email", "password"]  # 회원가입 시 입력 받을 필드 (email, phone, password)

    objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = "유저"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
