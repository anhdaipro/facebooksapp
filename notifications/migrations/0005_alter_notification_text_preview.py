# Generated by Django 3.2.4 on 2022-06-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_remove_notification_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='text_preview',
            field=models.TextField(blank=True, max_length=90),
        ),
    ]