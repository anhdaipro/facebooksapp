# Generated by Django 3.2.4 on 2022-06-14 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
    ]
