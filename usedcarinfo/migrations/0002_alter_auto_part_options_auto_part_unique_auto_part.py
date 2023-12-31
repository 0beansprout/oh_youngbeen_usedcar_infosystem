# Generated by Django 4.1 on 2023-05-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usedcarinfo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="auto_part",
            options={"ordering": ["auto_part_number", "auto_part_name"]},
        ),
        migrations.AddConstraint(
            model_name="auto_part",
            constraint=models.UniqueConstraint(
                fields=("auto_part_number", "auto_part_name"), name="unique_auto_part"
            ),
        ),
    ]
