# Generated by Django 5.1.4 on 2024-12-12 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_institution_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="state",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="main.state"
            ),
        ),
    ]
