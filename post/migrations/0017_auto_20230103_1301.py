# Generated by Django 3.2.16 on 2023-01-03 13:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_post_caption_edited_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='visible',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
