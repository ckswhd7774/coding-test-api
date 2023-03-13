# Generated by Django 4.1.4 on 2023-03-13 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("answer", "0001_initial"),
        ("explanation", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="explanation",
            options={"ordering": ["-created_at"], "verbose_name": "해설", "verbose_name_plural": "해설"},
        ),
        migrations.AddField(
            model_name="explanation",
            name="answer",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="answer.answer"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="explanation",
            name="text",
            field=models.TextField(default=1, verbose_name="내용"),
            preserve_default=False,
        ),
    ]
