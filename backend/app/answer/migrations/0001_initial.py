# Generated by Django 4.1.4 on 2023-03-12 18:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("question", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("text", models.TextField(verbose_name="내용")),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="question.question")),
            ],
            options={
                "verbose_name": "답",
                "verbose_name_plural": "답",
                "db_table": "answer",
                "ordering": ["-created_at"],
            },
        ),
    ]