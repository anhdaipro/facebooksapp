# Generated by Django 3.2.4 on 2022-06-22 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_alter_searchcurrent_user_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchcurrent',
            name='keyword',
            field=models.TextField(max_length=90, null=True),
        ),
    ]
