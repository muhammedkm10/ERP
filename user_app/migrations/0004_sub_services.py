# Generated by Django 5.1.3 on 2024-11-12 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0003_services"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sub_Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sub_service_name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "service_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.services",
                    ),
                ),
            ],
        ),
    ]