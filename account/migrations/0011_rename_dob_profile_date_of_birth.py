# Generated by Django 3.2.16 on 2022-12-30 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20221228_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]
