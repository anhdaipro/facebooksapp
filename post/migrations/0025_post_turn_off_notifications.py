# Generated by Django 3.2.4 on 2022-06-30 03:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0024_auto_20220630_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='turn_off_notifications',
            field=models.ManyToManyField(blank=True, related_name='turn_off_notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
