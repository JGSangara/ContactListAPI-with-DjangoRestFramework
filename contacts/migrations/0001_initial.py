# Generated by Django 4.1.3 on 2022-12-01 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("country_code", models.CharField(max_length=30)),
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("phone_number", models.CharField(max_length=30)),
                (
                    "contact_picture",
                    models.ImageField(null=True, upload_to="contact_pictures"),
                ),
                ("is_favorite", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
