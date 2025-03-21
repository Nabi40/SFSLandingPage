# Generated by Django 5.1.6 on 2025-03-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="hero",
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
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="cover_image/"),
                ),
                (
                    "tab_image",
                    models.ImageField(blank=True, null=True, upload_to="tab_image/"),
                ),
                ("tab_title", models.CharField(max_length=255)),
                ("tab_description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
