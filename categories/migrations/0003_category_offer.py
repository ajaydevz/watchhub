# Generated by Django 4.2.6 on 2024-01-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='offer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
