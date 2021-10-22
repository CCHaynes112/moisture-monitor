# Generated by Django 3.0.8 on 2021-10-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MoistureLevel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saturated", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
