# Generated by Django 4.1.4 on 2023-03-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submit_answer", "0004_submitanswer_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submitanswer",
            name="is_correct",
            field=models.BooleanField(default=False, verbose_name="정답 유무"),
        ),
    ]
