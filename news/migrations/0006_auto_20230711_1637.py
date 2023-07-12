# Generated by Django 3.2.19 on 2023-07-11 16:37

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20230711_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField()),
                ('platform', models.CharField(max_length=20)),
                ('release_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='release_image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='release_name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='release_platform',
        ),
    ]
