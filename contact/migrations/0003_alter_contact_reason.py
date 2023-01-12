# Generated by Django 3.2.16 on 2023-01-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_message_body_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('1', 'Login issue'), ('2', 'Report a post'), ('3', 'General Enquiry'), ('4', 'Delete Account')], default='3', max_length=2),
        ),
    ]
