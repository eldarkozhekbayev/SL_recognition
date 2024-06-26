# Generated by Django 5.0.4 on 2024-04-23 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Alphabet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("letter", models.CharField(max_length=5)),
                ("photo", models.ImageField(upload_to="alphabet_photos/")),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Language.language",
                    ),
                ),
            ],
        ),
    ]
