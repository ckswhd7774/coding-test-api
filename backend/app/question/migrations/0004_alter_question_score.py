# Generated by Django 4.1.4 on 2023-03-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question", "0003_alter_questioncategory_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="score",
            field=models.PositiveSmallIntegerField(default=0, verbose_name="점수"),
        ),
    ]
