# Generated by Django 3.2.16 on 2022-12-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_delete_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption_edited',
            field=models.BooleanField(default=False),
        ),
    ]
