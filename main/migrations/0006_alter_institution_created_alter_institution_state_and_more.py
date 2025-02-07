# Generated by Django 5.1.4 on 2024-12-12 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_institution_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="created",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="institution",
            name="state",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="main.state"
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="updated",
            field=models.DateTimeField(),
        ),
    ]
