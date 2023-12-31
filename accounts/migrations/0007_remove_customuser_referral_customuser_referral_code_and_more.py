# Generated by Django 4.2.6 on 2024-01-05 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_customuser_referral"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="referral",
        ),
        migrations.AddField(
            model_name="customuser",
            name="referral_code",
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="referrer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Payementwallet",
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
                    "paymenttype",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
