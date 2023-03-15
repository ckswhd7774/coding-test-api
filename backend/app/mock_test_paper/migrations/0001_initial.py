# Generated by Django 4.1.4 on 2023-03-15 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("question", "0003_alter_questioncategory_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="MockTestPaper",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("title", models.CharField(max_length=64, verbose_name="시험지 명")),
                ("question", models.ManyToManyField(blank=True, null=True, to="question.question")),
            ],
            options={
                "verbose_name": "모의고사 문제지",
                "verbose_name_plural": "모의고사 문제지",
                "db_table": "mock_test_paper",
                "ordering": ["-created_at"],
            },
        ),
    ]
