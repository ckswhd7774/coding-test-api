# Generated by Django 4.1.4 on 2023-03-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submit_answer", "0002_submitanswer_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="submitanswer",
            name="score",
            field=models.PositiveSmallIntegerField(default=1, verbose_name="점수"),
            preserve_default=False,
        ),
    ]
