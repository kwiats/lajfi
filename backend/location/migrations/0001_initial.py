# Generated by Django 5.0.6 on 2024-05-25 15:05

import django.db.models.deletion
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoricalLocation",
            fields=[
                ("ip_address", models.GenericIPAddressField(verbose_name="Adres IP")),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical location",
                "verbose_name_plural": "historical locations",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalTag",
            fields=[
                ("ip_address", models.GenericIPAddressField(verbose_name="Adres IP")),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                ("name", models.CharField(db_index=True, max_length=50)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical tag",
                "verbose_name_plural": "historical tags",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="locations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="locations", to="location.tag"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
