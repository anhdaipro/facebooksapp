# Generated by Django 3.2.4 on 2022-06-28 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0019_alter_post_viewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportfilepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=2000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('filepost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.fileuploadpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Filepost_emotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(choices=[('like', 'like'), ('love', 'love'), ('wow', 'wow'), ('sad', 'sad'), ('smile', 'smile'), ('indignant', 'indignant')], max_length=10)),
                ('created', models.DateTimeField(auto_now=True)),
                ('filepost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filepost', to='post.fileuploadpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]