# Generated by Django 4.1.4 on 2023-03-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submit_answer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="submitanswer",
            name="text",
            field=models.TextField(default=1, verbose_name="내용"),
            preserve_default=False,
        ),
    ]