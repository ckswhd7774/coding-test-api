# Generated by Django 4.1.4 on 2023-03-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question", "0003_alter_questioncategory_name"),
        ("mock_test_paper", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mocktestpaper",
            name="question",
            field=models.ManyToManyField(blank=True, to="question.question"),
        ),
    ]
