# Generated by Django 3.2.4 on 2022-06-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20220621_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='count_read_unseen_message',
        ),
        migrations.AddField(
            model_name='member',
            name='is_seen',
            field=models.BooleanField(default=True),
        ),
    ]
