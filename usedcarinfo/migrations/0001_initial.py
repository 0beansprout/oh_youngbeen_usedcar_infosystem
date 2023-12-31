# Generated by Django 4.1 on 2023-05-02 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Auto_part",
            fields=[
                ("auto_part_id", models.AutoField(primary_key=True, serialize=False)),
                ("auto_part_number", models.CharField(max_length=20)),
                ("auto_part_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=45)),
                ("last_name", models.CharField(max_length=45)),
                (
                    "disambiguator",
                    models.CharField(blank=True, default="", max_length=45),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Date",
            fields=[
                ("date_id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Dealer",
            fields=[
                ("dealer_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=45)),
                ("last_name", models.CharField(max_length=45)),
                (
                    "disambiguator",
                    models.CharField(blank=True, default="", max_length=45),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                ("inventory_id", models.AutoField(primary_key=True, serialize=False)),
                ("car_name", models.CharField(max_length=20)),
                (
                    "dealer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inventory",
                        to="usedcarinfo.dealer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Month",
            fields=[
                ("month_id", models.AutoField(primary_key=True, serialize=False)),
                ("month", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Period",
            fields=[
                ("period_id", models.AutoField(primary_key=True, serialize=False)),
                ("period_sequence", models.IntegerField(unique=True)),
                ("period_name", models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Technician",
            fields=[
                ("technician_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=45)),
                ("last_name", models.CharField(max_length=45)),
                (
                    "disambiguator",
                    models.CharField(blank=True, default="", max_length=45),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Year",
            fields=[
                ("year_id", models.AutoField(primary_key=True, serialize=False)),
                ("year", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Maintenance_schedule",
            fields=[
                (
                    "maintenance_schedule_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance_schedule",
                        to="usedcarinfo.date",
                    ),
                ),
                (
                    "month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance_schedule",
                        to="usedcarinfo.month",
                    ),
                ),
                (
                    "period",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance_schedule",
                        to="usedcarinfo.period",
                    ),
                ),
                (
                    "year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance_schedule",
                        to="usedcarinfo.year",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Maintenance",
            fields=[
                ("maintenance_id", models.AutoField(primary_key=True, serialize=False)),
                ("maintenance_name", models.CharField(max_length=20)),
                (
                    "auto_part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance",
                        to="usedcarinfo.auto_part",
                    ),
                ),
                (
                    "maintenance_schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance",
                        to="usedcarinfo.maintenance_schedule",
                    ),
                ),
                (
                    "technician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="maintenance",
                        to="usedcarinfo.technician",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("invoice_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="invoice",
                        to="usedcarinfo.customer",
                    ),
                ),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="invoice",
                        to="usedcarinfo.inventory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="inventory",
            name="maintenance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="inventory",
                to="usedcarinfo.maintenance",
            ),
        ),
    ]
