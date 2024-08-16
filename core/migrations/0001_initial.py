# Generated by Django 5.1 on 2024-08-14 20:34

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConsultWeather",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("temperature", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LogConsultWhather",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("data", models.JSONField()),
                (
                    "data_hash",
                    models.CharField(editable=False, max_length=64, unique=True),
                ),
                ("request_code", models.UUIDField()),
                (
                    "consult",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.consultweather",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
