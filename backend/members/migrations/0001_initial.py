# Generated for the initial FindMate members schema.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("display_name", models.CharField(max_length=80)),
                ("birth_date", models.DateField()),
                ("city", models.CharField(blank=True, max_length=100)),
                ("bio", models.TextField(blank=True, max_length=600)),
                ("interests", models.CharField(blank=True, max_length=300)),
                ("visible", models.BooleanField(default=False)),
                ("approved", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="match_profile", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("recipient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="likes_received", to=settings.AUTH_USER_MODEL)),
                ("sender", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="likes_sent", to=settings.AUTH_USER_MODEL)),
            ],
            options={"constraints": [models.UniqueConstraint(fields=("sender", "recipient"), name="unique_like")]},
        ),
        migrations.CreateModel(
            name="Block",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("blocked", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="blocks_received", to=settings.AUTH_USER_MODEL)),
                ("blocker", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="blocks_made", to=settings.AUTH_USER_MODEL)),
            ],
            options={"constraints": [models.UniqueConstraint(fields=("blocker", "blocked"), name="unique_block")]},
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("reason", models.CharField(max_length=300)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("reported", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reports_received", to=settings.AUTH_USER_MODEL)),
                ("reporter", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reports_made", to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
