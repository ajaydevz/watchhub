# Generated by Django 4.2.6 on 2024-01-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='referral',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
