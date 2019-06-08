# Generated by Django 2.2.2 on 2019-06-08 11:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idol_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='image',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='idol_item',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
