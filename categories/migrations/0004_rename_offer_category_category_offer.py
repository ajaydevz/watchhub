# Generated by Django 4.2.6 on 2024-01-04 10:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0003_category_offer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="offer",
            new_name="category_offer",
        ),
    ]
