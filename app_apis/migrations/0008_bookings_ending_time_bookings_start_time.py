# Generated by Django 5.1.3 on 2024-11-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_apis", "0007_client_requirements"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookings",
            name="ending_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="bookings",
            name="start_time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
