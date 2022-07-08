# Generated by Django 3.2.4 on 2022-06-24 15:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20220623_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hide_post',
            field=models.ManyToManyField(blank=True, related_name='hide_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='hide_story',
            field=models.ManyToManyField(blank=True, related_name='hide_story', to=settings.AUTH_USER_MODEL),
        ),
    ]
