# Generated by Django 5.1.3 on 2024-11-13 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_apis", "0001_initial"),
        ("user_app", "0004_sub_services"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                ("client_name", models.CharField(max_length=50)),
                ("client_phone_1", models.BigIntegerField()),
                ("client_phone_2", models.BigIntegerField(blank=True, null=True)),
                ("client_address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Bookings",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("totol_amount", models.IntegerField()),
                ("balance_amount", models.IntegerField()),
                (
                    "owner_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_details",
                        to="user_app.shopowners",
                    ),
                ),
                (
                    "clinet_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_apis.clients",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booked_Sub_Services",
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
                (
                    "booked_sub_services",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.sub_services",
                    ),
                ),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking",
                        to="app_apis.bookings",
                    ),
                ),
            ],
        ),
    ]