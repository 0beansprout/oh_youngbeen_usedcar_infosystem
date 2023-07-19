# Generated by Django 4.1 on 2023-05-03 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usedcarinfo", "0004_rename_period_month_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={"ordering": ["last_name", "first_name", "disambiguator"]},
        ),
        migrations.AlterModelOptions(
            name="dealer",
            options={"ordering": ["last_name", "first_name", "disambiguator"]},
        ),
        migrations.AlterModelOptions(
            name="inventory",
            options={"ordering": ["maintenance", "car_name", "dealer"]},
        ),
        migrations.AlterModelOptions(
            name="invoice",
            options={"ordering": ["inventory", "customer"]},
        ),
        migrations.AlterModelOptions(
            name="maintenance",
            options={
                "ordering": ["auto_part", "maintenance_name", "maintenance_schedule"]
            },
        ),
        migrations.AlterModelOptions(
            name="technician",
            options={"ordering": ["last_name", "first_name", "disambiguator"]},
        ),
        migrations.AddConstraint(
            model_name="customer",
            constraint=models.UniqueConstraint(
                fields=("last_name", "first_name", "disambiguator"),
                name="unique_customer",
            ),
        ),
        migrations.AddConstraint(
            model_name="dealer",
            constraint=models.UniqueConstraint(
                fields=("last_name", "first_name", "disambiguator"),
                name="unique_dealer",
            ),
        ),
        migrations.AddConstraint(
            model_name="inventory",
            constraint=models.UniqueConstraint(
                fields=("dealer", "maintenance", "car_name"), name="unique_inventory"
            ),
        ),
        migrations.AddConstraint(
            model_name="invoice",
            constraint=models.UniqueConstraint(
                fields=("inventory", "customer"), name="unique_invoices"
            ),
        ),
        migrations.AddConstraint(
            model_name="maintenance",
            constraint=models.UniqueConstraint(
                fields=("maintenance_schedule", "auto_part", "maintenance_name"),
                name="unique_maintenance",
            ),
        ),
        migrations.AddConstraint(
            model_name="technician",
            constraint=models.UniqueConstraint(
                fields=("last_name", "first_name", "disambiguator"),
                name="unique_technician",
            ),
        ),
    ]