# Generated by Django 3.2.4 on 2022-06-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20220615_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='duration',
            field=models.FloatField(default=0),
        ),
    ]