# Generated by Django 4.1.4 on 2023-03-15 16:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("question", "0003_alter_questioncategory_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="MockExam",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("score", models.IntegerField(verbose_name="점수")),
                ("start_time", models.DateTimeField(default=django.utils.timezone.now, verbose_name="시작 시간")),
                ("end_time", models.DateTimeField(default=django.utils.timezone.now, verbose_name="종료 시간")),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="question.question")),
            ],
            options={
                "verbose_name": "모의고사 문제",
                "verbose_name_plural": "모의고사 문제",
                "db_table": "mock_exam",
                "ordering": ["-created_at"],
            },
        ),
    ]
