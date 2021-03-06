# Generated by Django 3.2.4 on 2022-06-21 09:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_profile_count_notify_unseen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_info',
        ),
        migrations.AddField(
            model_name='profile',
            name='friend_invitation',
            field=models.ManyToManyField(blank=True, related_name='friend_invitation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobby',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='single',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='story',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='university',
            field=models.TextField(blank=True, null=True),
        ),
    ]
