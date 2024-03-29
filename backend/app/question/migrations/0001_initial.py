# Generated by Django 4.1.4 on 2023-03-12 18:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QuestionCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("name", models.CharField(max_length=32, verbose_name="유형 이름")),
            ],
            options={
                "verbose_name": "문제 유형",
                "verbose_name_plural": "문제 유형",
                "db_table": "question_category",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("title", models.CharField(max_length=64, verbose_name="제목")),
                ("text", models.TextField(verbose_name="내용")),
                ("restrictions", models.TextField(blank=True, null=True, verbose_name="제한 사항")),
                ("level", models.PositiveSmallIntegerField(verbose_name="난이도")),
                ("score", models.PositiveSmallIntegerField(verbose_name="점수")),
                ("submit_count", models.IntegerField(default=0, verbose_name="응시 횟수")),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="question.questioncategory"),
                ),
            ],
            options={
                "verbose_name": "문제",
                "verbose_name_plural": "문제",
                "db_table": "question",
                "ordering": ["-created_at"],
            },
        ),
    ]
