# Generated by Django 5.1.3 on 2024-11-13 15:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_apis", "0002_clients_bookings_booked_sub_services"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookings",
            old_name="totol_amount",
            new_name="total_amount",
        ),
    ]