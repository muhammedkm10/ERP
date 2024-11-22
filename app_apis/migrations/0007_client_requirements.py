# Generated by Django 5.1.3 on 2024-11-18 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_apis", "0006_rename_clinet_id_bookings_client_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client_requirements",
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
                ("img1", models.FileField(blank=True, null=True, upload_to="")),
                ("img2", models.FileField(blank=True, null=True, upload_to="")),
                ("img3", models.FileField(blank=True, null=True, upload_to="")),
                ("img4", models.FileField(blank=True, null=True, upload_to="")),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_apis.bookings",
                    ),
                ),
            ],
        ),
    ]
