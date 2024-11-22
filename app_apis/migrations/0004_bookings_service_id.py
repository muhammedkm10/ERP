# Generated by Django 5.1.3 on 2024-11-13 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_apis", "0003_rename_totol_amount_bookings_total_amount"),
        ("user_app", "0004_sub_services"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookings",
            name="service_id",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_app.services",
            ),
            preserve_default=False,
        ),
    ]
