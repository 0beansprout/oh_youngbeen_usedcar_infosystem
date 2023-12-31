# Generated by Django 4.1 on 2023-05-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usedcarinfo", "0003_alter_date_options_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Period",
            new_name="Month",
        ),
        migrations.AlterModelOptions(
            name="maintenance_schedule",
            options={
                "ordering": ["year__year", "month__period_sequence", "date__date"]
            },
        ),
        migrations.RemoveConstraint(
            model_name="maintenance_schedule",
            name="unique_maintenance_schedule",
        ),
        migrations.RenameField(
            model_name="maintenance_schedule",
            old_name="period",
            new_name="month",
        ),
        migrations.RenameField(
            model_name="month",
            old_name="period_id",
            new_name="month_id",
        ),
        migrations.AddConstraint(
            model_name="maintenance_schedule",
            constraint=models.UniqueConstraint(
                fields=("year", "month", "date"), name="unique_maintenance_schedule"
            ),
        ),
    ]
