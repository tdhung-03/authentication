# Generated by Django 4.2.5 on 2023-09-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]