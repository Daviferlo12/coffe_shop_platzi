# Generated by Django 5.1.3 on 2024-12-11 04:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order_product",
            old_name="orden",
            new_name="order",
        ),
    ]