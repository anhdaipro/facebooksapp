# Generated by Django 3.2.4 on 2022-06-16 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20220617_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='seen',
        ),
    ]