# Generated by Django 4.2.6 on 2023-12-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(max_length=50)),
                ('banner_image', models.ImageField(default=None, upload_to='photos/banner/')),
                ('banner_count', models.IntegerField(default=1)),
            ],
        ),
    ]